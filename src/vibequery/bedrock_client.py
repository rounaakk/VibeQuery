"""Generate one Redshift SQL statement per question via the Bedrock Converse API."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from vibequery.models import GenStatus

if TYPE_CHECKING:
    import boto3

    from vibequery.config import BedrockSettings


@dataclass
class GenerationResult:
    status: GenStatus
    sql: str
    error: str
    latency_ms: int
    input_tokens: int | None
    output_tokens: int | None
    raw_text: str


class BedrockSqlGenerator:
    """Calls ``bedrock-runtime`` ``converse``. ``generate`` records API failures and does not raise them."""

    def __init__(self, session: boto3.Session, settings: BedrockSettings, system_prompt: str) -> None:
        raise NotImplementedError

    def generate(self, question: str) -> GenerationResult:
        raise NotImplementedError
