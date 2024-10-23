import streamlit as st

# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Function to generate chatbot response (you can replace this with any chatbot logic)
def get_chatbot_response(user_input):
    # Replace this with actual chatbot logic or API call
    return f"Chatbot: I received your message: '{user_input}'"

# Streamlit App layout
st.title("Chatbot Interface")

# Chat history display
st.subheader("Chat History")
for message in st.session_state["chat_history"]:
    st.write(message)

# User input area
user_input = st.text_input("You:", key="user_input")

# On message send
if st.button("Send"):
    if user_input:
        # Display user's message and chatbot response
        st.session_state["chat_history"].append(f"You: {user_input}")
        chatbot_response = get_chatbot_response(user_input)
        st.session_state["chat_history"].append(chatbot_response)

# Add a clear chat button
if st.button("Clear Chat"):
    st.session_state["chat_history"] = []

