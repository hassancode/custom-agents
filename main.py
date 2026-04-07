from dotenv import load_dotenv

import content_agent
import context_object
import function_tool
import math_agent
import starter_agent
import multi_agent

load_dotenv()

AGENT = 6  # 1: starter_agent, 2: math_agent, 3: function_tool, 4: context_object, 5: content_agent


def main():
    if AGENT == 1:
        starter_agent.main()
    elif AGENT == 2:
        math_agent.main()
    elif AGENT == 3:
        function_tool.main()
    elif AGENT == 4:
        context_object.main()
    elif AGENT == 5:
        content_agent.main()
    elif AGENT == 6:
        multi_agent.main()


if __name__ == "__main__":
    main()

