# ob 🤖

ob is an autonomous organizational insights agent that thinks, plans, and learns as it works. It performs analysis using task planning, self‑reflection, and knowledge‑graph search. Think Claude Code, but focused on organizational knowledge and discovery.


## Overview

ob turns complex organizational questions into clear, step‑by‑step research plans. It runs those tasks using tools (like a knowledge‑graph search), checks its own work, and refines the results until it has a confident, data‑backed answer.

It’s not just another chatbot. It plans ahead, verifies progress, and iterates until the job is done.

**Key Capabilities:**
- **Intelligent Task Planning**: Decomposes complex queries into structured research steps
- **Autonomous Tool Use**: Selects and executes the right tools (Graphiti search)
- **Self‑Validation**: Checks its own work and iterates until tasks are complete
- **Knowledge Graph Search**: Query across nodes/edges/communities with strategies like RRF/MMR
- **Safety Features**: Loop detection and step limits to prevent runaway execution

[![Twitter Follow](https://img.shields.io/twitter/follow/virattt?style=social)](https://twitter.com/virattt)

## Quick Start

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- OpenAI API key
- Optional: Graphiti local API key and group IDs (for knowledge‑graph search)

### Installation

1. Install dependencies with uv:
```bash
uv sync
```

2. Set up your environment variables:
```bash
# Copy the example environment file
cp env.example .env

# Edit .env and add your keys (examples)
# OPENAI_API_KEY=your-openai-api-key
# GRAPHITI_API_KEY=your-graphiti-api-key
# GROUP_ID=group-1,group-2
# OB_LLM_MODEL=gpt-4o
# OB_ANSWER_LLM_MODEL=gpt-5-mini
# OB_MAX_STEPS=20
# OB_MAX_STEPS_PER_TASK=5
```

### Usage

Run ob in interactive mode:
```bash
uv run agent-ob
```

### Example Queries

Try asking ob questions like:
- "What meetings related to growth happened in the last 2 weeks?"
- "Who owns TikTok marketing and what’s the current strategy?"
- "Summarize the latest docs about our pricing changes."
- "Find contradictions between our product usage notes and dashboard metrics."

ob will automatically:
1. Break down your question into research tasks
2. Use tools (e.g., Graphiti search) to gather data
3. Validate if each task is sufficiently answered
4. Provide a concise, data‑rich final answer

## Architecture

ob follows a multi‑phase agent loop with specialized prompts:

- **Planning**: Analyze the query and produce a structured task list
- **Action**: Select and execute tools to make progress
- **Validation**: Decide if the task is sufficiently complete
- **Answering**: Synthesize a concise, data‑backed response

## Project Structure

```
ob/
├── src/
│   ├── ob/
│   │   ├── agent.py      # Main agent orchestration logic
│   │   ├── model.py      # LLM interface + prompt assembly
│   │   ├── tools.py      # LangChain tools (Graphiti search)
│   │   ├── graphiti.py   # HTTP adapter for knowledge-graph API
│   │   ├── prompts.py    # System prompts for each phase
│   │   ├── schemas.py    # Pydantic models for structured IO
│   │   ├── utils/        # UI, logger, and intro banner
│   │   └── cli.py        # CLI entry point (interactive REPL)
├── pyproject.toml
└── uv.lock
```

## Configuration

Configure via both the `Agent` constructor and environment variables.

```python
from ob.agent import Agent

agent = Agent(
    max_steps=20,              # Global safety limit
    max_steps_per_task=5       # Per-task iteration limit
)
```

Environment variables (see `env.example`):
- `OPENAI_API_KEY` (required)
- `GRAPHITI_API_KEY` (optional; local Graphiti API key)
- `GROUP_ID` (optional; single or comma‑separated default group IDs)
- `OB_LLM_MODEL` (default: `gpt-4o`)
- `OB_ANSWER_LLM_MODEL` (default: `gpt-5-mini`)
- `OB_MAX_STEPS`, `OB_MAX_STEPS_PER_TASK` (guardrails)

Graphiti backend defaults to `http://127.0.0.1:8000` (see `src/ob/graphiti.py`). Change in code if your API runs elsewhere.

## How to Contribute

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

**Important**: Please keep your pull requests small and focused. This makes review and merge easier.


## License

This project is licensed under the MIT License.
