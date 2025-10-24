import os, sys, json, asyncio
from datetime import datetime
from dotenv import load_dotenv
from dedalus_labs import AsyncDedalus, DedalusRunner

load_dotenv(".env")

def today():
    return datetime.now().strftime("%Y-%m-%d")

async def run_with_retry(runner, *, prompt, servers, model="openai/gpt-5", attempts=3):
    for i in range(attempts):
        try:
            return await runner.run(input=prompt, model=model, mcp_servers=servers, stream=False)
        except Exception:
            if i == attempts - 1:
                raise
            await asyncio.sleep(0.8 * (i + 1))  # brief backoff

async def main():
    q = sys.argv[1] if len(sys.argv) > 1 else "Summarize latest reporting and decide YES or NO with one-sentence rationale."
    key = os.getenv("DEDALUS_API_KEY")
    if not key:
        print(json.dumps({"error":"DEDALUS_API_KEY missing"})); return

    server = os.getenv("BRAVE_MCP", "windsor/brave-search-mcp")
    c = AsyncDedalus(api_key=key)
    r = DedalusRunner(c)

    prompt = f"""
You are a planning agent. Date: {today()}.
User task: {q}

You MUST use Brave Search MCP first to gather 3–6 recent sources.
Output format:
PLAN: one paragraph of what you searched and why.
EVIDENCE: 3–6 bullets with title, outlet, date YYYY-MM-DD, URL.
VERDICT: YES or NO, with one sentence rationale.
TOOLS_USED: list actual tools used.

Do not fabricate sources; include dates and links.
"""
    res = await run_with_retry(r, prompt=prompt, servers=[server], model="openai/gpt-5")
    print(json.dumps({
        "final_output": res.final_output,
        "tool_calls": getattr(res, "tool_calls", None)
    }, ensure_ascii=False))

if __name__ == "__main__":
    asyncio.run(main())
