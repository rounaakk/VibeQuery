"""Run one statement on Redshift Serverless through the Redshift Data API."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from vibequery.models import ExecStatus

if TYPE_CHECKING:
    import boto3

    from vibequery.config import RedshiftSettings


@dataclass
class ExecutionResult:
    status: ExecStatus
    error: str
    statement_id: str
    columns: list[str]
    rows: list[list]
    row_count: int
    truncated: bool
    latency_ms: int


class RedshiftDataApiExecutor:
    """Execute, poll, and fetch. Timeouts cancel the statement. API failures are returned, not raised."""

    def __init__(self, session: boto3.Session, settings: RedshiftSettings) -> None:
        raise NotImplementedError

    def execute(self, sql: str) -> ExecutionResult:
        raise NotImplementedError


def _field_value(field: dict) -> object:
    """Map one Data API field to a Python value. ``isNull`` becomes None."""
    raise NotImplementedError
