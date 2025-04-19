from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os
from agno.playground import Playground, serve_playground_app


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
AGNO_API_KEY = os.getenv("AGNO_API_KEY")

if not (GROQ_API_KEY and AGNO_API_KEY):
    raise ValueError("Please provide proper API key credentials")
    exit(1)


flowchart_agent = Agent(
    name="flowchart_agent",
    role="get flowchart information",
    model=Groq(id="llama-3.3-70b-versatile",api_key=GROQ_API_KEY),
    tools=[DuckDuckGoTools()],
    instructions=[],
    markdown=True,
)

app = Playground(agents=[flowchart_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)