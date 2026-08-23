"""Import the libraries required across all 16 weeks."""

from importlib import import_module
from importlib.metadata import PackageNotFoundError, version

MODULES = {
    "FastAPI": ("fastapi", "fastapi"),
    "Pydantic": ("pydantic", "pydantic"),
    "OpenAI SDK": ("openai", "openai"),
    "python-dotenv": ("dotenv", "python-dotenv"),
    "Tenacity": ("tenacity", "tenacity"),
    "HTTPX": ("httpx", "httpx"),
    "ChromaDB": ("chromadb", "chromadb"),
    "Rank BM25": ("rank_bm25", "rank-bm25"),
    "LangGraph": ("langgraph", "langgraph"),
    "LangChain Core": ("langchain_core", "langchain-core"),
    "MCP": ("mcp", "mcp"),
    "pytest": ("pytest", "pytest"),
    "pytest-asyncio": ("pytest_asyncio", "pytest-asyncio"),
    "Ruff": ("ruff", "ruff"),
}


def main() -> None:
    failures: list[str] = []
    for label, (module_name, package_name) in MODULES.items():
        try:
            import_module(module_name)
            package_version = version(package_name)
        except (ImportError, PackageNotFoundError) as exc:
            failures.append(f"{label}: {exc}")
        else:
            print(f"[OK] {label}: {package_version}")

    if failures:
        raise SystemExit("\n".join(f"[FAIL] {failure}" for failure in failures))

    print("[OK] All 16-week Python dependencies are importable.")


if __name__ == "__main__":
    main()
