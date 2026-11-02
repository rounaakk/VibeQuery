"""System prompt for Redshift SQL generation. The schema document is inserted verbatim."""

from __future__ import annotations

SYSTEM_PROMPT_TEMPLATE = """You are an expert data analyst who writes SQL for Amazon Redshift.
All tables live in Amazon Redshift. Use only Redshift-compatible SQL syntax and functions;
Redshift is PostgreSQL-derived but does not support every PostgreSQL feature.

Rules:
- Use ONLY the tables and columns described in the schema document below. Never invent tables or columns.
- Always schema-qualify table names exactly as written in the schema document.
- Produce exactly one read-only statement (SELECT or WITH ... SELECT). No DDL/DML.
- Prefer explicit column lists over SELECT *.
- If the question cannot be answered from the schema, respond with
  <cannot_answer>short reason</cannot_answer> and nothing else.
- Otherwise respond with the SQL wrapped in <sql></sql> tags and nothing else.

<schema_document>
{schema}
</schema_document>"""


def build_system_prompt(schema: str, template: str | None = None) -> str:
    """Insert ``schema`` with ``str.replace``, not ``str.format`` (schemas may contain braces)."""
    raise NotImplementedError


def build_user_message(question: str) -> str:
    """Return the user turn for one question."""
    raise NotImplementedError
