# Media feed

Podcasts and videos made from the vault go into a private podcast feed. A podcast app on the phone subscribes to it, so episodes play with the screen locked and keep their place. Git ignores media files, because GitHub rejects files over 100 MB and every device would download every episode.

## Publish an episode

```bash
uv run .tools/media-feed/publish.py "99 - Attachments/Podcasts/<file>.mp3" --title "Title" --about "One line on what it is"
```

The script uploads the file, rebuilds `feed.xml`, and prints the episode URL. Link that URL from the note the episode came from (`[▶ Listen](url)`), then commit and push the note.

- `--backfill` publishes every media file in the vault that is not in the feed yet.
- `--feed-url` prints the address to paste into the podcast app.

## How the feed stays private

The feed is a folder in a storage bucket. The folder has a long random name (`MEDIA_PREFIX`). Anyone with the full feed link can play the episodes, but nobody can list the bucket or guess the folder name, and the feed asks podcast directories not to index it. This is the same privacy as an unlisted YouTube video. Treat the feed link like a password: never put it, or the prefix, in the repo.

`episodes.json` in the folder lists every episode. The script rebuilds the feed from it on every publish, and its `source` field (the file's path in the vault) stops a file from being published twice.

## Storage options

Both options cost little or nothing for a personal feed. The setup prompt (`SETUP.md`) walks through either one.

- **Amazon S3.** Well under US$1 a month for a personal feed. Needs an AWS account. Make the bucket readable only under the random folder, and give the publishing key write access to that bucket only.
- **Cloudflare R2.** Free up to 10 GB with no download charges. Needs a Cloudflare account. Turn on the bucket's public `r2.dev` URL, and set `MEDIA_S3_ENDPOINT` to `https://<account id>.r2.cloudflarestorage.com` and `MEDIA_REGION` to `auto`.

## Settings

All settings go in `~/.config/learning-vault/.env` or the environment:

| Setting | What it is |
|---|---|
| `MEDIA_BUCKET` | The bucket name |
| `MEDIA_PREFIX` | The random folder name, at least 24 letters and digits |
| `MEDIA_PUBLIC_URL` | The bucket's public base URL, such as `https://<bucket>.s3.<region>.amazonaws.com` or `https://pub-<id>.r2.dev` |
| `MEDIA_REGION` | The AWS region, or `auto` for R2 |
| `MEDIA_S3_ENDPOINT` | R2 or another S3-compatible store only |
| `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | The publishing key (R2 issues keys in the same format) |
| `MEDIA_AWS_PROFILE` | Use a named AWS CLI profile instead of the two keys above |
| `MEDIA_FEED_TITLE` | The feed's name in the podcast app (default `Vault`) |
