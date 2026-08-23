import sys
from pathlib import Path

import chromadb
import fastapi
import langgraph
import mcp
import openai


def test_python_version_is_311() -> None:
    assert sys.version_info[:2] == (3, 11)


def test_interpreter_is_project_local() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    assert Path(sys.prefix).resolve() == (repo_root / ".venv").resolve()


def test_core_dependencies_import() -> None:
    assert all((chromadb, fastapi, langgraph, mcp, openai))
