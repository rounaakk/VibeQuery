"""Load the Markdown schema document that is placed whole into the system prompt."""

from __future__ import annotations

from pathlib import Path


def load_schema(path: Path) -> str:
    """Read UTF-8 text and strip it. Fail if empty.

    Warn when the rough token estimate (``len(text) / 4``) exceeds 150_000.
    """
    raise NotImplementedError
