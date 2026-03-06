import asyncio

from agents import Agent, function_tool, run_demo_loop


@function_tool
def add(a: float, b: float) -> float:
    return a + b


@function_tool
def multiply(a: float, b: float) -> float:
    return a * b


@function_tool
def divide(a: float, b: float) -> str:
    if b == 0:
        return "Error: division by zero"
    return str(a / b)


agent = Agent(
    name="Math Agent",
    instructions="You are a math assistant. Use your tools to perform calculations.",
    model="gpt-4o-mini",
    tools=[add, multiply, divide],
)


def main():
    asyncio.run(run_demo_loop(agent))
