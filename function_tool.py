import asyncio

from agents import Agent, function_tool, run_demo_loop


@function_tool
def get_current_time() -> str:
    from datetime import datetime
    return datetime.now().isoformat()


@function_tool
def add_task(name: str, priority: int) -> str:
    return f"Task '{name}' added with priority {priority}."


agent = Agent(
    name="Function Tool Agent",
    instructions="You are a helpful assistant that demonstrates basic function calling.",
    model="gpt-4o-mini",
    tools=[get_current_time, add_task],
)


def main():
    asyncio.run(run_demo_loop(agent))
