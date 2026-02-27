from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()

agent = Agent(
    name="My Agent",
    instructions="You are a helpful assistant that can answer questions.",
    model="gpt-4o-mini"
)

def main():
    result = Runner.run_sync(agent, "What is the capital of France?")
    print(result.final_output)

if __name__ == "__main__":
    main()
