import asyncio

from agents import Agent, run_demo_loop

agent = Agent(
    name="Starter Agent",
    instructions="You are a helpful assistant that can answer questions.",
    model="gpt-4o-mini",
)


def main():
    asyncio.run(run_demo_loop(agent))
