import os
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv
from dedalus_labs.utils.streaming import stream_async
import asyncio

load_dotenv()

async def main():
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    result = runner.run(
        input="serach the web for what elon musk said lately tell me if u used the tools",
        model=["gpt-5", "claude-sonnet-4-20250514"],
        mcp_servers=["windsor/brave-search-mcp"],
        stream=True
    )
 
    await stream_async(result)

if __name__ == "__main__":
    asyncio.run(main())