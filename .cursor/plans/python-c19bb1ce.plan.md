<!-- c19bb1ce-f944-49a7-9bb0-463130498f08 fad3732f-485c-4d3f-92b1-729cfe08fce0 -->
# Orchestration MCP (Python) – Plan

## What we'll build

A Python orchestrator that, given parsed market context (title, category, expiry), dynamically selects marketplace MCP servers and prompts a model to use them via Dedalus SDK. It returns a structured result: per-source findings + aggregated judgment.

## Key decisions

- Use `dedalus-labs` Python SDK with async runner.
- Read `DEDALUS_API_KEY` from `.env` (no keys in code).
- Config-driven routing: simple rules mapping market type → MCP servers.
- Start with heuristic weighting; later swap for learned weights.

## Files to add

- `orchestrator/requirements.txt` – `dedalus-labs`, `python-dotenv`, `pydantic`
- `orchestrator/.env.example` – `DEDALUS_API_KEY=...`
- `orchestrator/config.yml` – routing rules + marketplace MCP slugs
- `orchestrator/types.py` – Pydantic models for input/output
- `orchestrator/router.py` – select MCP servers per context
- `orchestrator/prompts.py` – task-specific prompt templates
- `orchestrator/run_orchestration.py` – main async orchestration logic
- `orchestrator/cli.py` – CLI: `--context` JSON or inline args

## Config shape (excerpt)

```yaml
# orchestrator/config.yml
model: "openai/gpt-4o-mini"
marketplace_servers:
  brave: "tsion/brave-search-mcp"
  twitter: "REPLACE_WITH_TWITTER_MCP"
  reddit: "REPLACE_WITH_REDDIT_MCP"
  google_news: "REPLACE_WITH_GOOGLE_NEWS_MCP"
  youtube: "REPLACE_WITH_YOUTUBE_MCP"
  linkedin: "REPLACE_WITH_LINKEDIN_MCP"
routing:
  political: [twitter, reddit, google_news, linkedin]
  crypto: [twitter, reddit, brave]
  tech: [linkedin, google_news, reddit, youtube]
  default: [brave, google_news]
```

## Minimal orchestration call (core logic)

```python
# orchestrator/run_orchestration.py (core snippet)
from dedalus_labs import AsyncDedalus, DedalusRunner

async def orchestrate(context, model, mcp_servers, system_prompt, stream=False):
    client = AsyncDedalus()
    runner = DedalusRunner(client)
    result = await runner.run(
        input=system_prompt.render(context=context),
        model=model,
        mcp_servers=mcp_servers,
        stream=stream,
    )
    return result.final_output
```

## Flow

1) Parse context JSON (from Screenshot Analyzer output).

2) Router chooses MCP servers via `config.yml` + heuristics.

3) Build targeted prompt instructing the model to call only provided tools and return structured JSON per source.

4) Run via Dedalus; capture tool results.

5) Aggregate to a single probability + rationale.

6) Return `OrchestrationResult` (context, selected_servers, per-source findings, final_score, confidence).

## CLI usage

- `python -m orchestrator.cli --context path/to/context.json`
- or: `python -m orchestrator.cli --title "Will ETH > $5k by Dec 31?" --category crypto --expiry 2025-12-31`

## Next.js handoff (later)

Optional endpoint: `app/app/api/orchestrate/route.ts` to call the Python CLI/process and stream results to the UI.

### To-dos

- [ ] Create orchestrator folder and Python requirements + dotenv scaffold
- [ ] Add config.yml with marketplace MCP slugs and routing rules
- [ ] Define Pydantic models for input context and orchestration output
- [ ] Implement router selecting MCP servers by market type
- [ ] Create prompts that tell model to use only provided tools and return JSON
- [ ] Implement async run_orchestration using DedalusRunner with selected MCPs
- [ ] Aggregate per-source outputs into weighted probability and confidence
- [ ] Add CLI to load context, run orchestration, print JSON
- [ ] Confirm/replace placeholder marketplace slugs for Twitter/Reddit/News/YouTube/LinkedIn
- [ ] (Optional) Add Next.js API route to invoke orchestrator