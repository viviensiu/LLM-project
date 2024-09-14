
import streamlit as st
# import time
# from llm import LLM
from rag import RAG

llm_options = {"1":"OpenAI GPT-4o-mini", "2":"Ollama Microsoft Phi3" }
st.title("AZ900 Study Buddy")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "bot" not in st.session_state:
    st.session_state.bot = None
# if "counter" not in st.session_state:
#     st.session_state.counter = 0


# st.markdown(
#     """
# <style>
#     .st-emotion-cache-4oy321 {
#         display: flex;
#         flex-direction: row-reverse;
#         text-align: right;
#     }
# </style>
# """,
#     unsafe_allow_html=True,
# )

# html style to allow chatbot style mimic OpenAI's style
# user query on the right and response on the left
st.html(
    """
<style>
    .stChatMessage:has(.chat-user) {
        flex-direction: row-reverse;
        text-align: right;
    }
</style>
"""
)

# Sidebar Okay!
with st.sidebar:
    with st.form("llm form", clear_on_submit=True):
        model_choice = st.selectbox("Choose an LLM Model for this chatbot",
                        options=list(llm_options.keys()), format_func=lambda x:llm_options[x])
        apikey = st.text_input(f'Input your LLM API key here', type='password')
        button = st.form_submit_button("Submit")
        if button:
            # replace with llm initialization 
            st.session_state.bot = RAG(model_choice, apikey)
            # st.sidebar.markdown(bot.model)
            # st.sidebar.markdown(bot.apikey)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.html(f"<span class='chat-{message['role']}'></span>")
        st.markdown(message["content"])

# React to user input
if query := st.chat_input("It's time to study for your AZ900 exam!"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.html(f"<span class='chat-user'></span>")
        st.markdown(query)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})
    # st.session_state.counter += 1

    # Spinner to indicate processing query
    with st.spinner("Hmmm..."):
        response = None
        # time.sleep(2)
        # response = f"Echo: {st.session_state.counter}"
        if st.session_state.bot:
            response, _, _ = st.session_state.bot.rag(query)
        else:
            response = "Please set your LLM model first!"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# issue: cannot use form_submit_button in sidebar.form
# with st.sidebar.form("llm form", clear_on_submit=True):
#     llm = st.sidebar.selectbox("Choose an LLM Model for this chatbot",
#                     options=list_LLM)
#     apikey = st.sidebar.text_input(f'Input your {llm} API key here', type='password')
#     button = st.sidebar.button("Submit")
#     if button:
#         st.sidebar.markdown(llm)
#         st.sidebar.markdown(apikey)

