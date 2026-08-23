# AI Agent 16 周学习工作区

这是与《AI Agent 零基础就业实战教程》配套的独立项目。项目固定使用 uv 管理的 Python 3.11，不读取或修改电脑里其他 Python 项目的虚拟环境。

## 每次开始学习

在 PowerShell 中运行：

```powershell
cd D:\Agent\ai-agent-road
uv run python scripts/check_environment.py
```

运行项目命令时统一写成 `uv run ...`，例如：

```powershell
uv run pytest -q
uv run ruff check .
uv run uvicorn apps.ticket_api.main:app --reload
```

`.env` 已创建，但只有占位值。取得 API Key 后只编辑 `.env`，不要把真实密钥写进代码或提交到 Git。
