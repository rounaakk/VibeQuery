"""Reject anything other than a single read-only SELECT or WITH statement."""

from __future__ import annotations


def validate_read_only(sql: str) -> str | None:
    """Return an error message, or None when ``sql`` is safe to run.

    Requires one statement whose type is SELECT or WITH, and rejects a
    denylist of write and admin keywords after comments are stripped.
    """
    raise NotImplementedError
