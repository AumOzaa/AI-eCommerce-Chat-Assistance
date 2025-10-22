from Utilities.agent import agent
import asyncio


async def chat():
    while True:
        user_input = input("You : ")
        output = await agent.run(user_input)
        print("Agent :", output)

asyncio.run(chat())