import streamlit as st
import time
from typing import Optional
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os
from agno.playground import Playground, serve_playground_app
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.utils.pprint import pprint_run_response

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
AGNO_API_KEY = os.getenv("AGNO_API_KEY")
MODEL = 'llama-3.3-70b-versatile'

if not (GROQ_API_KEY and AGNO_API_KEY):
    raise ValueError("Please provide proper API key credentials")
    exit(1)



flowchart_agent = Agent(
    name="flowchart_agent",
    role="get flowchart information",
    model=Groq(id=MODEL,api_key=GROQ_API_KEY),
    tools=[DuckDuckGoTools()],
    instructions="""
    You are a professional Senio God level full stack Developer. Designed countless SaaS application products and have 1000+ hours of experience in the field.
    You are also a expert in the field of flowchart and diagram. Design flowchart and diagrams for the applications that based on the user's request.
    You also know a lot about the latest technologies frameworks and trends in the field of software development.
    Your current role is to design flowchart and diagrams for the applications that based on the user's request.
    The designs you create should be professional and modern. 
    They must be written in the proper language syntax of mermaid markdown format.
    Based on the user's request, you will design the flowchart and diagrams for the applications.
    They can be in different styles such as using the flowchart, graph, sequence diagram, etc.
    The flowcahrts create must be in the proper language syntax of mermaid markdown format. and should be rendered properly.
    """,
    markdown=True,
)


# Page config
st.set_page_config(
    page_title="AI Agent Chat",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("AI Agent Settings")
    
    # Agent selection
    agent = st.selectbox(
        "Select AI Agent",
        ["flowchart_agent"],
        index=0
    )

    MODEL = st.selectbox(
        "Select Model",
        ["llama-3.3-70b-versatile", "llama-3.3-8b-versatile"],
        index=0
    )
    
    # API Status
    st.subheader("API Status")
    status_placeholder = st.empty()
    
    # Simulate API status check
    def check_api_status():
        status_placeholder.info("Checking API status...")
        time.sleep(1)  # Simulate API check
        status_placeholder.success("API Connected ✅")
    
    check_api_status()

# Main content area
st.title("AI Agent Chat Interface")

# Chat input
user_input = st.text_area(
    "Enter your message",
    placeholder="Type your message here...",
    height=100
)

# Generate button
if st.button("Generate Response", type="primary"):
    if user_input:
        with st.spinner("Generating response..."):
            # Clear previous messages
            st.session_state.messages = []
            
            # Add user message to chat
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Get AI response
            response_stream: Iterator[RunResponse] = flowchart_agent.run(user_input, stream=True)
            pprint_run_response(response_stream)
    
    else:
        st.warning("Please enter a message first!")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
