# Custom Agents

A simple AI agent built with the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python).

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and replace `your-api-key-here` with your actual key.

## Usage

```bash
uv run main.py
```

## Stack

- Python 3.9+
- [openai-agents](https://github.com/openai/openai-agents-python)
- Model: `gpt-4o-mini`
