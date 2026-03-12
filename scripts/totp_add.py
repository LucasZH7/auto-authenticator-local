#!/usr/bin/env python3
"""Store a TOTP seed in macOS Keychain."""

from __future__ import annotations

import argparse
import sys

from totp_common import normalize_seed
from totp_keychain import store_seed


def main() -> int:
    parser = argparse.ArgumentParser(description="Store a TOTP seed in macOS Keychain.")
    parser.add_argument("--alias", required=True, help="Short local alias for the account.")
    parser.add_argument("--seed", required=True, help="Base32 TOTP seed.")
    parser.add_argument("--issuer", default="", help="Optional issuer label.")
    parser.add_argument("--account", default="", help="Optional account label.")
    args = parser.parse_args()

    try:
        seed = normalize_seed(args.seed)
        store_seed(args.alias, seed, issuer=args.issuer, account=args.account)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Stored alias '{args.alias}' in macOS Keychain.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
