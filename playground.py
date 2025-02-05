from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
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

# Web searching agent
web_search_agent = Agent(
    name="web_agent",
    role="search the web for information based on the user given input",
    model=Groq(id="llama-3.3-70b-versatile",api_key=GROQ_API_KEY),
    tools=[
        DuckDuckGoTools()
    ],
    show_tool_calls=False,
    markdown=True,
)

financial_agent = Agent(
    name="financial_agent",
    role="get financial information",
    model=Groq(id="llama-3.3-70b-versatile",api_key=GROQ_API_KEY),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)
    ],
    instructions=[
        "Please provide the stock ticker symbol you would like to get information on",
        "use tables to display the data",
    ],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[web_search_agent, financial_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)