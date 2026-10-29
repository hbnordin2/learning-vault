# /// script
# requires-python = ">=3.11"
# dependencies = ["boto3>=1.34"]
# ///
"""Publish audio or video to the private podcast feed, for listening on the phone.

Git can't hold large media, and Obsidian is a poor player, so anything worth
listening to or watching goes into a podcast feed instead. The phone subscribes
to the feed in a podcast app (AntennaPod on Android, Podcast Addict, Overcast or
Pocket Casts), which plays with the screen locked and remembers the position.

    uv run .tools/media-feed/publish.py FILE [--title "Episode title"] [--about "One line"]
    uv run .tools/media-feed/publish.py --backfill     # every media file in the vault not yet published
    uv run .tools/media-feed/publish.py --feed-url     # print the feed URL to subscribe to

Prints the episode's URL so it can be linked from the note it came from.

Configuration comes from the environment, or from ~/.config/learning-vault/.env
(see .tools/media-feed/README.md):
  MEDIA_BUCKET         the S3 (or S3-compatible) bucket name
  MEDIA_PREFIX         a long random folder name; it is what keeps the feed private
  MEDIA_PUBLIC_URL     the bucket's public base URL, e.g. https://<bucket>.s3.<region>.amazonaws.com
  MEDIA_REGION         e.g. us-east-1 (optional for Cloudflare R2: use "auto")
  MEDIA_S3_ENDPOINT    only for S3-compatible stores such as Cloudflare R2
  AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY, or MEDIA_AWS_PROFILE
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import mimetypes
import os
import re
import subprocess
import sys
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape

VAULT = Path(__file__).resolve().parents[2]
MEDIA = {".mp3": "audio/mpeg", ".m4a": "audio/mp4", ".m4b": "audio/mp4",
         ".wav": "audio/wav", ".mp4": "video/mp4", ".m4v": "video/mp4", ".mov": "video/quicktime"}
SKIP_DIRS = {".git", ".obsidian", ".trash", ".tools", "node_modules"}
FEED_DESCRIPTION = "Podcasts and videos generated from the Obsidian vault."


def load_dotenv() -> None:
    """Read ~/.config/learning-vault/.env. Variables already set win."""
    path = Path.home() / ".config" / "learning-vault" / ".env"
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def config():
    load_dotenv()
    missing = [k for k in ("MEDIA_BUCKET", "MEDIA_PREFIX", "MEDIA_PUBLIC_URL") if not os.environ.get(k)]
    if missing:
        sys.exit(f"{', '.join(missing)} not set; see .tools/media-feed/README.md")
    bucket = os.environ["MEDIA_BUCKET"]
    prefix = os.environ["MEDIA_PREFIX"].strip("/")
    public = os.environ["MEDIA_PUBLIC_URL"].rstrip("/")
    return f"{public}/{prefix}", bucket, os.environ.get("MEDIA_REGION") or None, prefix


def s3_client(region: str | None):
    import boto3

    endpoint = os.environ.get("MEDIA_S3_ENDPOINT") or None
    profile = os.environ.get("MEDIA_AWS_PROFILE")
    if profile and not os.environ.get("AWS_ACCESS_KEY_ID"):
        return boto3.Session(profile_name=profile).client("s3", region_name=region, endpoint_url=endpoint)
    return boto3.client("s3", region_name=region, endpoint_url=endpoint)


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:80] or "episode"


def duration_seconds(path: Path) -> int:
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
        return int(float(out))
    except Exception:
        return 0


def load_index(s3, bucket: str, prefix: str) -> list[dict]:
    try:
        body = s3.get_object(Bucket=bucket, Key=f"{prefix}/episodes.json")["Body"].read()
        return json.loads(body)
    except s3.exceptions.NoSuchKey:
        return []
    except s3.exceptions.ClientError as err:
        # Some S3-compatible stores answer a missing key with a bare 404.
        if err.response.get("Error", {}).get("Code") in ("404", "NoSuchKey"):
            return []
        raise


def build_feed(episodes: list[dict], base: str) -> str:
    items = []
    for ep in sorted(episodes, key=lambda e: e["published"], reverse=True):
        published = format_datetime(dt.datetime.fromisoformat(ep["published"]))
        items.append(f"""    <item>
      <title>{escape(ep['title'])}</title>
      <description>{escape(ep.get('about', ''))}</description>
      <enclosure url="{escape(ep['url'])}" length="{ep['size']}" type="{ep['type']}"/>
      <guid isPermaLink="false">{escape(ep['key'])}</guid>
      <pubDate>{published}</pubDate>
      <itunes:duration>{ep.get('duration', 0)}</itunes:duration>
    </item>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <title>{escape(os.environ.get("MEDIA_FEED_TITLE", "Vault"))}</title>
    <link>{escape(base)}/feed.xml</link>
    <description>{FEED_DESCRIPTION}</description>
    <language>en</language>
    <itunes:block>Yes</itunes:block>
    <itunes:explicit>false</itunes:explicit>
{chr(10).join(items)}
  </channel>
</rss>
"""


def publish(paths: list[Path], title: str | None, about: str | None) -> None:
    base, bucket, region, prefix = config()
    s3 = s3_client(region)
    episodes = load_index(s3, bucket, prefix)
    known = {ep.get("source") for ep in episodes}

    for path in paths:
        path = path.resolve()
        content_type = MEDIA.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0]
        if not content_type or not content_type.startswith(("audio/", "video/")):
            sys.exit(f"Not an audio or video file: {path}")
        try:
            source = path.relative_to(VAULT).as_posix()
        except ValueError:
            source = path.name
        if source in known:
            print(f"Already published: {source}")
            continue
        ep_title = title or " ".join(path.stem.replace("_", " ").replace("-", " ").split())
        stamp = dt.datetime.now(dt.timezone.utc)
        key = f"{prefix}/episodes/{stamp:%Y%m%d-%H%M%S}-{slugify(ep_title)}{path.suffix.lower()}"
        print(f"Uploading {source} ...", flush=True)
        s3.upload_file(str(path), bucket, key, ExtraArgs={"ContentType": content_type})
        url = f"{base}/{quote(key.removeprefix(prefix + '/'))}"
        episodes.append({
            "title": ep_title,
            "about": about or f"From the vault: {source}",
            "source": source,
            "key": key,
            "url": url,
            "type": content_type,
            "size": path.stat().st_size,
            "duration": duration_seconds(path),
            "published": stamp.isoformat(timespec="seconds"),
        })
        known.add(source)
        print(f"  episode: {url}", flush=True)

    s3.put_object(Bucket=bucket, Key=f"{prefix}/episodes.json",
                  Body=json.dumps(episodes, indent=2).encode(), ContentType="application/json")
    s3.put_object(Bucket=bucket, Key=f"{prefix}/feed.xml", Body=build_feed(episodes, base).encode(),
                  ContentType="application/rss+xml; charset=utf-8", CacheControl="max-age=60")
    print(f"Feed: {base}/feed.xml")


def vault_media() -> list[Path]:
    found = [
        p for p in VAULT.rglob("*")
        if p.is_file() and p.suffix.lower() in MEDIA
        and not any(part in SKIP_DIRS for part in p.relative_to(VAULT).parts)
    ]
    # An .m4b audiobook is usually a chaptered copy of an .mp3 beside it.
    stems = {(p.parent, p.stem) for p in found if p.suffix.lower() != ".m4b"}
    return sorted(p for p in found if not (p.suffix.lower() == ".m4b" and (p.parent, p.stem) in stems))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--title")
    parser.add_argument("--about")
    parser.add_argument("--backfill", action="store_true")
    parser.add_argument("--feed-url", action="store_true")
    args = parser.parse_args()

    if args.feed_url:
        print(f"{config()[0]}/feed.xml")
        return
    paths = vault_media() if args.backfill else args.files
    if not paths:
        parser.error("give a file to publish, or --backfill")
    if args.title and len(paths) > 1:
        parser.error("--title only works with a single file")
    publish(paths, args.title, args.about)


if __name__ == "__main__":
    main()
