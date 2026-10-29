# Setup instructions for the agent

These are instructions for a coding agent (Codex, Claude Code, or similar) that is setting up this vault for its owner. The owner pasted the prompt from `README.md`, which pointed you here. Follow the steps in order.

## How to work with the owner

- The owner is a researcher, not a programmer. Run every command yourself. Ask the owner to act only for things an agent must not or cannot do: creating accounts, signing in, typing a password, paying, approving a browser prompt, and steps on the phone.
- Ask one question at a time, in plain words. Before each step, say in a sentence what it does and why it is needed.
- Never ask the owner to paste an API key or password into the chat. Keys go into the secrets file (step 5), which you open in a text editor for the owner to fill in.
- Ask before anything that costs money, and say what it costs.
- If a step fails, read the error, fix the cause, and explain the fix in a sentence. Do not skip a step silently: if one cannot be done, say so and continue with the rest.
- On Windows, use PowerShell. `~` means `$env:USERPROFILE`.

## 1. Ask the owner

Ask these, one at a time, and keep the answers for later steps:

1. Is this the **first device** being set up, or does the vault already exist on GitHub (setting up another laptop)? If it already exists, ask for the repository name.
2. What kind of **phone**: iPhone or Android?
3. **Podcasts** need a voice service. ElevenLabs gives the best voices on a paid plan (see elevenlabs.io/pricing; about four hour-long episodes a month needs the Creator plan). OpenAI's voices cost less per episode but need a separate OpenAI API account (a ChatGPT subscription does not include API credit). Which one, or none for now?
4. Should podcasts reach the **phone's podcast app**? This needs a small storage bucket: Amazon S3 (well under US$1 a month) or Cloudflare R2 (free up to 10 GB). Both need an account and a payment card on file. Which one, or skip for now? Without it, episodes are still saved on the laptop.
5. Should **flashcards** go to Anki? Anki is free on computers and Android (AnkiDroid). The iPhone app (AnkiMobile) is a one-off purchase.

## 2. Install the programs

Check what is already installed first (`git --version`, `gh --version`, `uv --version`, `ffmpeg -version`), and install only what is missing.

**macOS.** If Homebrew is missing, install it from brew.sh. The installer asks for the computer's password: tell the owner to type it in the terminal window. Then:

```bash
brew install git gh uv ffmpeg poppler
brew install --cask obsidian
```

**Windows:**

```powershell
winget install --id Git.Git -e
winget install --id GitHub.cli -e
winget install --id astral-sh.uv -e
winget install --id Gyan.FFmpeg -e
winget install --id Obsidian.Obsidian -e
git config --global core.longpaths true
```

Open a new terminal afterwards so the new programs are on the PATH.

## 3. Connect GitHub and get the vault

Run `gh auth status`. If not signed in, run `gh auth login --web --git-protocol https` and ask the owner to finish the sign-in in the browser. If the owner has no GitHub account, ask them to create a free one at github.com/signup first. Then run `gh auth setup-git` so plain `git` uses the same sign-in.

Set the commit name and email if they are missing (`git config --global user.name`, `git config --global user.email`). Ask the owner for them.

**First device.** Ask the owner what to call the vault (suggest `vault`). Create a **private** copy of the template and download it into the Documents folder:

```bash
cd ~/Documents
gh repo create <name> --template hbnordin2/learning-vault --private --clone
```

The repository must be private: it will hold the owner's own notes. Check with `gh repo view <name> --json visibility`.

**Another device.** Download the existing vault: `cd ~/Documents && gh repo clone <name>`.

Work inside the vault folder from now on.

## 4. Set up Obsidian

Make sure Obsidian is closed. Then install the plugins (Git sync, Quiz Block for worksheets, and Obsidian_to_Anki if the owner wants Anki):

```bash
uv run .tools/setup/install_obsidian_plugins.py obsidian-git quizblock obsidian-to-anki-plugin
```

Leave out `obsidian-to-anki-plugin` if the owner skipped Anki. Then ask the owner to:

1. Open Obsidian, choose **Open folder as vault**, and pick the vault folder.
2. When Obsidian asks about community plugins, choose **Trust author and enable plugins** (or Settings → Community plugins → Turn on community plugins).

The Git plugin now pulls changes when Obsidian opens and every 10 minutes, and commits and pushes the owner's edits every 10 minutes.

## 5. Make the secrets file

Create the folder `~/.config/learning-vault/` and copy `.tools/learncast/.env.example` into it as `.env`. Set `LEARNCAST_TTS_PROVIDER` to the owner's choice from step 1.

**ElevenLabs.** Ask the owner to sign up at elevenlabs.io and choose a plan. Then: profile menu → **API Keys** → **Create API key**, with access to Text to Speech. Open the `.env` file in a text editor (`open -e ~/.config/learning-vault/.env` on macOS, `notepad $env:USERPROFILE\.config\learning-vault\.env` on Windows) and ask the owner to paste the key after `ELEVENLABS_API_KEY=` and save.

**OpenAI.** The same, with a key from platform.openai.com → API keys, pasted after `OPENAI_API_KEY=`.

Check that learncast can see the key:

```bash
cd .tools/learncast && uv sync && uv run learncast providers
```

Then make a short test episode (three or four lines, a few hundred credits) with `uv run learncast synth <test file> --title "Setup test" --no-vault`, and play it for the owner (`open` on macOS, `start` on Windows). Delete the test files afterwards.

## 6. The podcast feed (optional)

Skip this step if the owner skipped it in step 1.

Make a random folder name for the feed. It is what keeps the feed private:

```bash
uv run python -c "import secrets; print(secrets.token_hex(12))"
```

**Amazon S3.** Ask the owner to create an AWS account at aws.amazon.com if they have none. Install the AWS CLI (`brew install awscli`, or `winget install --id Amazon.AWSCLI -e`), and ask the owner to sign in with `aws configure sso` or an access key from the AWS console, whichever they prefer. Then, with a bucket name such as `<name>-vault-media-<4 random digits>` and the region nearest the owner:

1. Create the bucket: `aws s3api create-bucket --bucket <bucket> --region <region> --create-bucket-configuration LocationConstraint=<region>` (leave out `--create-bucket-configuration` for `us-east-1`).
2. Allow a bucket policy to grant public reads: `aws s3api put-public-access-block --bucket <bucket> --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false`.
3. Let anyone read objects inside the random folder only, so nobody can list the bucket: a bucket policy allowing `s3:GetObject` on `arn:aws:s3:::<bucket>/<prefix>/*` for `"Principal": "*"`.
4. Create an IAM user `vault-media-publisher` whose only permission is `s3:GetObject` and `s3:PutObject` on `arn:aws:s3:::<bucket>/<prefix>/*`, and make an access key for it.
5. Put the settings in the `.env` file: `MEDIA_BUCKET`, `MEDIA_PREFIX`, `MEDIA_REGION`, `MEDIA_PUBLIC_URL=https://<bucket>.s3.<region>.amazonaws.com`, and the publisher's `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. Open the file for the owner to paste the secret key, or write it yourself straight from the command output without showing it in the chat.

**Cloudflare R2.** Ask the owner to create a Cloudflare account and turn on R2 (it asks for a card even on the free tier). In the Cloudflare dashboard, guide them to create a bucket, turn on its **Public Development URL** (`r2.dev`), and create an R2 API token with Object Read & Write on that bucket only. Settings: `MEDIA_BUCKET`, `MEDIA_PREFIX`, `MEDIA_PUBLIC_URL=https://pub-<id>.r2.dev`, `MEDIA_REGION=auto`, `MEDIA_S3_ENDPOINT=https://<account id>.r2.cloudflarestorage.com`, and the token's Access Key ID and Secret Access Key as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. A public `r2.dev` URL lets anyone read any object whose name they know, so the random folder name is the only privacy, as with S3.

Test it: publish a short test MP3 with `uv run .tools/media-feed/publish.py <file> --title "Setup test"`, then fetch the feed URL from `--feed-url` and check that the episode URL plays. Give the owner the feed URL in a way they can move to the phone (for example, email it to themselves), and tell them to treat it like a password.

## 7. The phone

Ask the owner to do these steps on the phone. Explain each one as they go.

1. Install **Obsidian** and **GitSync** (both free, App Store or Google Play).
2. In GitSync, sign in with GitHub, choose the vault repository, and let it download into a new folder. On iPhone, pick a folder inside **On My iPhone → Obsidian** so Obsidian can see it. On Android, any folder works.
3. In Obsidian, open that folder as a vault. Turn on community plugins, then browse and install **quizblock** (for worksheets). The Git and Anki plugins are not needed on the phone.
4. Make GitSync sync automatically. On Android, GitSync can sync when Obsidian opens and closes (follow its "sync on app open/close" setup). On iPhone, use the Shortcuts app: Automation → App → Obsidian → "Is Opened" and "Is Closed" → run GitSync's Sync action.
5. If step 6 was done: install a podcast app (AntennaPod on Android; Overcast, Pocket Casts or Apple Podcasts on iPhone) and add the feed by URL (Apple Podcasts: Library → ⋯ → Follow a Show by URL).
6. If Anki was chosen: install AnkiDroid or AnkiMobile and sign in with the same AnkiWeb account as the laptop.

## 8. Anki on the laptop (optional)

Skip this if the owner skipped Anki.

1. Install Anki (`brew install --cask anki`, or `winget install --id Anki.Anki -e`).
2. Ask the owner to open Anki, create a free AnkiWeb account when it offers sync, and install the **AnkiConnect** add-on: Tools → Add-ons → Get Add-ons → code `2055492159`. Restart Anki.
3. Check that it answers: `curl -s localhost:8765 -X POST -d '{"action":"version","version":6}'` (on Windows use `curl.exe` and escape the quotes, or Python). It should print a version number.
4. Explain to the owner: after the `learn` skill writes flashcards into a note, Anki must be open, and they press the Obsidian_to_Anki icon in Obsidian's left ribbon to send the cards. Anki then syncs them to the phone through AnkiWeb.

## 9. Connect the agents

**Network access.** Podcasts, the feed and `git push` need the internet. Codex blocks network access inside its sandbox by default. Explain this to the owner, then ask whether to allow it for this vault. If yes, add this to `~/.codex/config.toml`:

```toml
[sandbox_workspace_write]
network_access = true
```

If the owner prefers not to, Codex asks for approval each time a command needs the network.

**Codex.** Codex reads `AGENTS.md` and the skills in `.agents/skills/` whenever it is started in the vault folder. Show the owner how to start it there. They can type `$` to pick a skill, but asking in plain words works too.

**ChatGPT.** In ChatGPT's settings, the owner can connect GitHub and give it access to the vault repository. ChatGPT can then read the notes when asked about them. It cannot run the podcast tools, which need Codex on the laptop.

**Claude Code** (if the owner uses it): run `uv run .tools/setup/copy_skills_for_claude.py`.

## 10. Finish

1. Write a short note `00 - Inbox/Setup — <today's date>.md` that lists what was set up on this device and what was skipped. Commit and push it, and check that it arrives on GitHub (`gh repo view --web` opens the repository).
2. If the phone is set up, ask the owner to open Obsidian on the phone and look for the note. This proves the sync works in both directions once they edit it and you `git pull` it back.
3. Tell the owner, in plain sentences, what they can now ask for (the table in `AGENTS.md`), with one example each. Good first requests: "Write up this paper" with a PDF, "Make me a 45-minute podcast on the spacing effect", "Give me a worksheet on `01 - Projects/Learning/Foundations`".
4. Tell them what was skipped and that they can ask to set it up later by saying "finish the setup in SETUP.md".
