"""Settings loaded from CLI flags, environment variables, and an optional TOML file."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import boto3


class ConfigError(Exception):
    """Invalid or incomplete configuration. The CLI exits with code 2."""


@dataclass
class BedrockSettings:
    model_id: str = ""
    max_tokens: int = 2048
    temperature: float = 0.0


@dataclass
class RedshiftSettings:
    workgroup: str = ""
    database: str = ""
    secret_arn: str | None = None
    max_rows: int = 1000
    query_timeout: int = 300
    allow_writes: bool = False


@dataclass
class AwsSettings:
    region: str | None = None
    profile: str | None = None


@dataclass
class Settings:
    mode: str
    input: Path
    output: Path
    overwrite: bool = False
    schema_path: Path | None = None
    system_prompt_path: Path | None = None
    results_dir: Path = field(default_factory=lambda: Path("results"))
    concurrency: int = 4
    verbose: bool = False
    bedrock: BedrockSettings = field(default_factory=BedrockSettings)
    redshift: RedshiftSettings = field(default_factory=RedshiftSettings)
    aws: AwsSettings = field(default_factory=AwsSettings)

    def validate(self) -> None:
        """Raise ConfigError when the active mode is missing required settings."""
        raise NotImplementedError


def load_settings(args: argparse.Namespace) -> Settings:
    """Merge TOML, environment variables, and CLI args. CLI wins. Then validate."""
    raise NotImplementedError


def make_session(aws: AwsSettings) -> boto3.Session:
    """Build a boto3 session from the configured profile and region."""
    raise NotImplementedError
