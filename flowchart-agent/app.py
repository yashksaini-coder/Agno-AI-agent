import streamlit as st
import time
from typing import Optional

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
        ["GPT-4", "Claude", "Gemini"],
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
            # Simulate API call
            time.sleep(2)
            
            # Add user message to chat
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Simulate AI response
            ai_response = f"This is a simulated response from {agent} to: {user_input}"
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
    
    else:
        st.warning("Please enter a message first!")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
