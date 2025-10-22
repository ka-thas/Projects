from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")


async def main():
    agent = Agent(
        task="open finn.no and find the cheapest bed in Oslo",
        llm=llm,
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
