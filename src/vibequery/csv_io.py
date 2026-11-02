"""Read question CSVs and write the output CSV plus per-query result CSVs."""

from __future__ import annotations

from pathlib import Path

from vibequery.models import QueryRecord


def read_records(path: Path, mode: str) -> list[QueryRecord]:
    """Load rows for ``mode`` (generate, execute, or all).

    Assigns filename-safe ids, rejects duplicates, and keeps unknown columns
    on ``QueryRecord.extra``. Execute mode also reads existing ``gen_*`` fields.
    """
    raise NotImplementedError


def write_records(path: Path, records: list[QueryRecord], overwrite: bool) -> None:
    """Write the output CSV atomically (temp file, then replace). Preserve input order."""
    raise NotImplementedError


def write_result_csv(path: Path, columns: list[str], rows: list[list]) -> None:
    """Write one query result set. NULL values are empty strings."""
    raise NotImplementedError
