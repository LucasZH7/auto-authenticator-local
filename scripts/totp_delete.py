#!/usr/bin/env python3
"""Delete a stored TOTP seed from macOS Keychain."""

from __future__ import annotations

import argparse
import sys

from totp_keychain import delete_seed


def main() -> int:
    parser = argparse.ArgumentParser(description="Delete a TOTP seed from macOS Keychain.")
    parser.add_argument("--alias", required=True, help="Stored alias.")
    args = parser.parse_args()

    try:
        delete_seed(args.alias)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Deleted alias '{args.alias}' from macOS Keychain.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
