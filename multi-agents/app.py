import groq
import os
from dotenv import load_dotenv
load_dotenv()

# AI assistant imports
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.agent import Agent, RunResponse
from agno.tools.wikipedia import WikipediaTools
from agno.tools.calculator import CalculatorTools

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = groq.Client(api_key=GROQ_API_KEY)

if not GROQ_API_KEY:
    raise ValueError("Please provide a GROQ API key")

# Enhanced web search agent with more capabilities
web_search_agent = Agent(
    name="web_agent",
    role="comprehensive web research and information gathering specialist",
    model=Groq(id="gemma2-9b-it", api_key=GROQ_API_KEY),
    tools=[
        DuckDuckGoTools(search=True, news=True),
        WikipediaTools(),
    ],
    instructions=[
        "You are an advanced web research specialist capable of handling complex queries",
        "Your primary objectives are to:",
        "1. Break down complex queries into manageable sub-tasks",
        "2. Gather information from multiple sources for comprehensive answers",
        "3. Verify information across different sources",
        "4. Provide well-structured, detailed responses with proper citations",
        "5. Handle ambiguous queries by asking clarifying questions when needed",
        "6. Maintain context throughout multi-step queries",
        "7. Format responses in clear, organized markdown with proper sections",
        "When dealing with complex queries:",
        "- Start by analyzing the query components",
        "- Identify required information sources",
        "- Gather data systematically",
        "- Synthesize information coherently",
        "- Provide clear reasoning for your conclusions"
    ]
)

# Enhanced financial agent with more capabilities
financial_agent = Agent(
    name="financial_agent",
    role="comprehensive financial analysis and advisory specialist",
    model=Groq(id="gemma2-9b-it", api_key=GROQ_API_KEY),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True, 
            company_info=True, 
            technical_indicators=True, 
            historical_prices=True,
            key_financial_ratios=True,
            income_statements=True,
        ),
        CalculatorTools(add=True,
            subtract=True,
            multiply=True,
            divide=True,
            exponentiate=True,
            factorial=True,
            is_prime=True,
            square_root=True,),
    ],
    instructions=[
        "You are an advanced financial analysis specialist with expertise in complex market analysis",
        "Your capabilities include:",
        "1. Comprehensive financial analysis and reporting",
        "2. Multi-factor investment analysis",
        "3. Market trend analysis and forecasting",
        "4. Risk assessment and portfolio optimization",
        "5. Detailed financial statement analysis",
        "6. Industry-specific financial insights",
        "7. Comparative analysis across companies and sectors",
        "When handling complex financial queries:",
        "- Break down complex financial concepts into understandable terms",
        "- Provide both quantitative and qualitative analysis",
        "- Include relevant market context and industry trends",
        "- Highlight key risks and opportunities",
        "- Support conclusions with data and analysis",
        "- Format responses with clear sections and visualizations when appropriate"
    ]
)

# Enhanced multi-agent system with better coordination
multi_ai = Agent(
    team=[web_search_agent, financial_agent],
    model=Groq(id="deepseek-r1-distill-llama-70b", api_key=GROQ_API_KEY),
    markdown=True,
    instructions=[
        "You are a coordinated team of specialized AI agents working together to handle complex queries",
        "Your coordination strategy includes:",
        "1. Identifying the primary domain of each query",
        "2. Assigning tasks to appropriate specialists",
        "3. Combining insights from multiple agents",
        "4. Ensuring consistent and coherent responses",
        "5. Handling cross-domain queries effectively",
        "6. Maintaining context across multiple interactions",
        "7. Providing comprehensive, well-structured responses",
        "When processing complex queries:",
        "- Analyze query complexity and requirements",
        "- Delegate tasks to appropriate specialists",
        "- Synthesize information from multiple sources",
        "- Ensure logical flow and coherence",
        "- Provide clear reasoning and evidence",
        "- Format responses for maximum clarity and usefulness"
    ]
)

# Example usage with error handling
try:
    response = multi_ai.print_response(
        "Analyze the current market trends and provide a comprehensive report on the AI sector's performance, including major companies' stock movements and recent news affecting the industry.",
        stream=True
    )
except Exception as e:
    print(f"An error occurred: {str(e)}")
    print("Please try rephrasing your query or check your API key.")
