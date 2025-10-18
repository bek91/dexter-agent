# uv + Python Project Cheat Sheet (macOS + Homebrew Python 3.13)

## Create a project

### A) Using `requirements.txt`

```bash
cd /path/to/project
uv venv --python /opt/homebrew/bin/python3
source .venv/bin/activate
uv pip install -r requirements.txt
```

### B) Using `pyproject.toml` (recommended)

```bash
cd /path/to/project
uv init
uv venv --python /opt/homebrew/bin/python3
source .venv/bin/activate
uv add fastapi uvicorn    # add whatever you need
```

## Run code (activation optional)

```bash
# Without activating the venv:
uv run python app.py
uv run python -m mypkg.module
```

## Manage dependencies

```bash
uv add <pkg>...           # add & install (writes to pyproject + lock)
uv remove <pkg>...
uv sync                   # install exactly what's in the lockfile

# requirements workflow
uv pip install -r requirements.txt
uv pip compile -o requirements.lock -r requirements.txt
```

## One-command bootstrap (you already added `pynew`)

Usage:

```bash
pynew cool-api fastapi uvicorn python-dotenv
# then:
uv run uvicorn cool_api.main:app --reload
```

## Per-project env vars (no global secrets)

**.env file (in project root):**

```
OPENAI_API_KEY=sk-...
```

**Option 1: load in code**

```python
from dotenv import load_dotenv
load_dotenv()  # reads .env
```

Run:

```bash
uv run python your_script.py
```

**Option 2: load in shell**

```bash
set -a; source .env; set +a
uv run python your_script.py
```

## Old projects with `python -m venv`

**Use as-is:**

```bash
cd /path/to/old-project
source .venv/bin/activate
pip install -r requirements.txt
```

**(Optional) Migrate to uv:**

```bash
cd /path/to/old-project
deactivate 2>/dev/null || true
rm -rf .venv
uv venv --python /opt/homebrew/bin/python3
source .venv/bin/activate
uv pip install -r requirements.txt
# or:
uv init --package
uv add -r requirements.txt
```

## Prompt naming

```bash
uv venv --prompt my-env      # set env name shown in your shell prompt
# or before activating:
export VIRTUAL_ENV_PROMPT="(my-env) "
source .venv/bin/activate
```

## Handy patterns

```bash
uvx ruff format .            # run a tool without installing it into the env
uvx pytest
python -c "import sys; print(sys.executable)"   # verify current interpreter
```

## Minimal `pyproject.toml`

```toml
[project]
name = "myproj"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = []

[tool.uv]
```

---

**Default workflow:** prefer **B (pyproject)** for new repos; use **A (requirements.txt)** when inheriting legacy projects.


## uv Essential commands
```md
# Project setup
uv init myproject           # Create new project
uv add requests             # Add dependency
uv remove requests             # Remove dependency
uv sync                     # Install from lockfile

# Running code
uv run script.py    # Run in project environment
uv run pytest              # Run tests

# Python management
uv python install 3.12     # Install Python version
uv python pin 3.12         # Set project Python

# Tool usage
uvx black .                # Run tool temporarily
uv tool install ruff       # Install tool globally

# Package management (pip-compatible)
uv pip install requests  # Direct pip replacement
uv pip install -r requirements.txt
```