#!/usr/bin/env python3
"""Thin wrappers around macOS Keychain for TOTP seeds."""

from __future__ import annotations

import subprocess

from totp_common import KEYCHAIN_SERVICE


def store_seed(alias: str, seed: str, issuer: str = "", account: str = "") -> None:
    label = f"{issuer} {account}".strip() or alias
    subprocess.run(
        [
            "security",
            "add-generic-password",
            "-U",
            "-a",
            alias,
            "-s",
            KEYCHAIN_SERVICE,
            "-l",
            label,
            "-w",
            seed,
        ],
        check=True,
        capture_output=True,
        text=True,
    )


def fetch_seed(alias: str) -> str:
    result = subprocess.run(
        [
            "security",
            "find-generic-password",
            "-a",
            alias,
            "-s",
            KEYCHAIN_SERVICE,
            "-w",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise KeyError(f"No TOTP seed found for alias '{alias}'.")
    return result.stdout.strip()


def delete_seed(alias: str) -> None:
    result = subprocess.run(
        [
            "security",
            "delete-generic-password",
            "-a",
            alias,
            "-s",
            KEYCHAIN_SERVICE,
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise KeyError(f"No TOTP seed found for alias '{alias}'.")
