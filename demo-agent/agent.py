from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Please provide a GROQ API key")
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

multiple_agents = Agent(
    team=[web_search_agent, financial_agent],
    model=Groq(id="llama-3.3-70b-versatile",api_key=GROQ_API_KEY),
    markdown=True,
    instructions=[
        "Always include and show source data",
        "Please provide the stock ticker symbol you would like to get information on",
        "use tables to display the data",
    ],
)


multiple_agents.print_response("summarize the stock market today for the stock AAPL")
