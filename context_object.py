import asyncio
from dataclasses import dataclass, field

from agents import Agent, RunContextWrapper, function_tool, run_demo_loop


@dataclass
class UserContext:
    name: str
    notes: list[str] = field(default_factory=list)


@function_tool
def save_note(ctx: RunContextWrapper[UserContext], note: str) -> str:
    ctx.context.notes.append(note)
    return f"Note saved: '{note}'"


@function_tool
def list_notes(ctx: RunContextWrapper[UserContext]) -> str:
    if not ctx.context.notes:
        return "No notes saved yet."
    return "\n".join(f"{i + 1}. {n}" for i, n in enumerate(ctx.context.notes))


@function_tool
def greet_user(ctx: RunContextWrapper[UserContext]) -> str:
    return f"Hello, {ctx.context.name}!"


agent = Agent(
    name="Context Agent",
    instructions="You are a personal assistant. Use your tools to greet the user and manage their notes.",
    model="gpt-4o-mini",
    tools=[greet_user, save_note, list_notes],
)


def main():
    context = UserContext(name="Hassan")
    asyncio.run(run_demo_loop(agent, context=context))
