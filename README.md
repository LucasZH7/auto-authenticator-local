# Auto Authenticator Local

Auto Authenticator Local is an OpenClaw skill and local toolset for generating TOTP codes from secrets stored on the same Mac.

It is built for legitimate account owners and authorized operators who want:

- local-only secret storage
- no cloud sync requirement
- explicit, on-demand 6-digit TOTP generation
- a simple OpenClaw-compatible skill folder they can install or publish

## Why this exists

Many people already use TOTP-based login prompts during approved automation or repetitive admin work. This project makes that workflow local, small, and auditable:

- TOTP seeds are stored in macOS Keychain
- codes are generated only when explicitly requested
- the implementation is pure Python plus the built-in `security` CLI
- no secrets are written to git or plaintext config files

## Safety boundary

This project is not for bypassing MFA policy, evading anti-abuse systems, or hiding OTP generation from security controls. It is meant for accounts the user personally owns or is explicitly authorized to manage.

## Features

- Store a TOTP seed under a short alias
- Generate a 6-digit code with remaining lifetime
- Delete aliases cleanly during rotation or offboarding
- Use the same folder as an OpenClaw skill
- Publishable to ClawHub as a transparent, local-first utility

## Requirements

- macOS
- Python 3.11+
- Access to the built-in `security` command
- OpenClaw only if you want the skill behavior inside OpenClaw

## Quick start

Store a seed:

```bash
python3 scripts/totp_add.py --alias github-work --issuer GitHub --account lucas@example.com --seed JBSWY3DPEHPK3PXP
```

Generate a code:

```bash
python3 scripts/totp_code.py --alias github-work
```

Delete an alias:

```bash
python3 scripts/totp_delete.py --alias github-work
```

## OpenClaw usage

Place this folder inside your workspace skills directory or install it through ClawHub later. The skill instructs the agent to use the bundled scripts explicitly and safely.

## Development

Run tests:

```bash
python3 -m unittest discover -s tests
```

## Publish notes

- GitHub repo: ready to publish as an open repository
- ClawHub: publish as a public skill with privacy-first tags and a compliant description
- Positioning: local TOTP helper, privacy-first, transparent, explicit, auditable
