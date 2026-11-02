"""Pull SQL or a cannot-answer reason out of a Bedrock response."""

from __future__ import annotations

from vibequery.models import GenStatus


def extract_sql(text: str) -> tuple[GenStatus, str, str]:
    """Return ``(status, sql, error)``.

    Prefer ``<cannot_answer>``, then ``<sql>``, then a ```sql fence.
    Strip whitespace and one trailing semicolon. Otherwise status is ERROR.
    """
    raise NotImplementedError
