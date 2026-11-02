"""Generate SQL, optionally execute it, and write the output CSV."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from vibequery.models import QueryRecord

if TYPE_CHECKING:
    from vibequery.bedrock_client import BedrockSqlGenerator
    from vibequery.config import Settings
    from vibequery.redshift_client import RedshiftDataApiExecutor


def generate_all(records: list[QueryRecord], generator: BedrockSqlGenerator, concurrency: int) -> None:
    """Fill generation fields in place. An empty question is a per-row error."""
    raise NotImplementedError


def execute_all(
    records: list[QueryRecord],
    executor: RedshiftDataApiExecutor,
    settings: Settings,
    results_dir: Path,
    concurrency: int,
) -> None:
    """Run readable SQL and write ``<results_dir>/<id>.csv``. Skip or block rows that must not run."""
    raise NotImplementedError


def run(settings: Settings) -> int:
    """Run the selected mode and return 0 when every row succeeded, else 1."""
    raise NotImplementedError
