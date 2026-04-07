from agents import Agent, Runner

base_researcher = Agent(
    name="Base Researcher",
    instructions="You are a helpful assistant that can research information on the web.",
    model="gpt-4o-mini"
)

tavily_researcher = Agent(
    name="Tavily Researcher",
    instructions="You are a helpful assistant that can research information on the web. You have access to the Tavily API for retrieving information.",
    model="gpt-4o-mini"
)

def main():
    topic = input("Enter a topic: ")
    #result = Runner.run_sync(base_researcher, topic)
    result = Runner.run_sync(tavily_researcher, topic)
    print(result.final_output)
    