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
        input="Find the year GPT-5 released, and handoff to Claude to write a haiku about Elon Musk. Output this haiku.",
        model=["gpt-5", "claude-sonnet-4-20250514"],
        stream=True
    )

    await stream_async(result)

if __name__ == "__main__":
    asyncio.run(main())