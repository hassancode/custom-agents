from agents import Agent, Runner

research_agent = Agent(
    name="Research Agent",
    instructions=(
        "You are a research specialist. Given a topic, gather and summarize key facts, "
        "background information, and relevant points. Return a structured research summary."
    ),
    model="gpt-4o-mini",
)

writer_agent = Agent(
    name="Writer Agent",
    instructions=(
        "You are a professional content writer. Given a research summary, write a clear, "
        "engaging, and well-structured piece of content. Return only the final written content."
    ),
    model="gpt-4o-mini",
)

coordinator_agent = Agent(
    name="Coordinator Agent",
    instructions=(
        "You are a content creation coordinator. When given a topic:\n"
        "1. Call the research tool to gather information on the topic.\n"
        "2. Call the writer tool with the research results to produce the final content.\n"
        "3. Present the final written content to the user."
    ),
    model="gpt-4o-mini",
    tools=[
        research_agent.as_tool(
            tool_name="research",
            tool_description="Research a topic and return a structured summary of key facts and information.",
        ),
        writer_agent.as_tool(
            tool_name="write",
            tool_description="Write engaging content based on a research summary. Pass the full research output as input.",
        ),
    ],
)


def main():
    topic = input("Enter a topic: ")
    result = Runner.run_sync(coordinator_agent, topic)
    print(result.final_output)
