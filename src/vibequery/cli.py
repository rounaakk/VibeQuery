"""Argument parsing and process exit codes for the VibeQuery CLI."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Flags are specified in docs/DESIGN.md section 3."""
    raise NotImplementedError


def main(argv: list[str] | None = None) -> None:
    """Parse arguments, load settings, and exit with the pipeline status code.

    ConfigError and FileNotFoundError exit with code 2.
    """
    raise NotImplementedError
