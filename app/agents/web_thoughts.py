# agents/web_thoughts.py
import os, sys, json, asyncio
from dotenv import load_dotenv
from dedalus_labs import AsyncDedalus, DedalusRunner

load_dotenv(".env")

async def main():
    q = sys.argv[1] if len(sys.argv) > 1 else "Analyze this bet for EV and risk. Cite sources."
    server = os.getenv("BRAVE_MCP", "windsor/brave-search-mcp")
    key = os.getenv("DEDALUS_API_KEY")
    if not key:
        print(json.dumps({"error":"DEDALUS_API_KEY missing"})); return
    c = AsyncDedalus(api_key=key)
    r = DedalusRunner(c)
    res = await r.run(input=q, model="openai/gpt-5", mcp_servers=[server], stream=False)
    print(json.dumps({"final_output": res.final_output, "tool_calls": getattr(res, "tool_calls", None)}, ensure_ascii=False))

if __name__ == "__main__":
    asyncio.run(main())
