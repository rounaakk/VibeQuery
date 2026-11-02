"""Row model and status values shared across the pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class GenStatus(StrEnum):
    OK = "ok"
    CANNOT_ANSWER = "cannot_answer"
    ERROR = "error"


class ExecStatus(StrEnum):
    OK = "ok"
    ERROR = "error"
    BLOCKED = "blocked"
    SKIPPED = "skipped"
    TIMEOUT = "timeout"


@dataclass
class QueryRecord:
    """One input question and the generation and execution fields written back to CSV."""

    id: str
    question: str = ""
    sql: str = ""
    gen_status: GenStatus | None = None
    gen_error: str = ""
    model_id: str = ""
    gen_latency_ms: int | None = None
    input_tokens: int | None = None
    output_tokens: int | None = None
    exec_status: ExecStatus | None = None
    exec_error: str = ""
    statement_id: str = ""
    row_count: int | None = None
    truncated: bool | None = None
    result_file: str = ""
    exec_latency_ms: int | None = None
    extra: dict[str, str] = field(default_factory=dict)
