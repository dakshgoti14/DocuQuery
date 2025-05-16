''' import streamlit as st
from utils.summarizer import summarize_text
from utils.ner import extract_entities
from utils.qa_engine import create_vector_store, create_qa_chain
from utils.file_handler import extract_text_from_file
from utils.auth import sign_up, sign_in, logout, check_login_status
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"
# Initialize session state
def initialize_session_state():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "new_chat" not in st.session_state:
        st.session_state.new_chat = False
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = None
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "LLaMA"

def start_new_chat():
    st.session_state.chat_history = []
    st.session_state.new_chat = True
    st.rerun()

def handle_logout():
    logout()
    st.session_state.logged_in = False
    st.session_state.username = None
    st.rerun()

# App title
st.title("📄 Smart Document Q&A Chatbot")

initialize_session_state()

# Sidebar layout
with st.sidebar:
    if st.session_state.logged_in:
        st.write(f"👋 Logged in as: `{st.session_state.username}`")
        
        if st.button("🆕 Start New Chat"):
            start_new_chat()
        if st.button("🚪 Logout"):
            handle_logout()

        st.write("### 💬 Chat History")
        if len(st.session_state.chat_history) > 0:
            for i, chat in enumerate(st.session_state.chat_history, 1):
                st.write(f"**Q{i}:** {chat['question']}")
                st.write(f"**A{i}:** {chat['answer']}")
        else:
            st.write("No chat history yet.")

        st.write("### 🧠 Choose a Model")
        selected_model = st.selectbox("Select a model:", ["LLaMA", "Bart"])
        st.session_state.selected_model = selected_model
    else:
        st.write("### 🔐 Sign Up / Sign In")
        option = st.radio("Choose:", ["Sign Up", "Sign In"])

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if option == "Sign Up":
            if st.button("Sign Up"):
                sign_up(username, password)
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
        elif option == "Sign In":
            if st.button("Sign In"):
                if sign_in(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()

# File upload and processing

uploaded_file = st.file_uploader("📎 Upload a document (TXT, PDF, DOCX)", type=["txt", "pdf", "docx"])

if uploaded_file and st.session_state.logged_in:
    file_type = uploaded_file.name.split('.')[-1].lower()
    text = extract_text_from_file(uploaded_file, file_type)

    # Summarize and extract entities
    summary = summarize_text(text)
    entities = extract_entities(text)

    st.write("### 📑 Document Summary")
    st.write(summary)

    # Create QA chain
    vector_store = create_vector_store(text)
    qa_chain = create_qa_chain(vector_store, st.session_state.selected_model)

    # Ask a question
    question = st.text_input("❓ Ask a question about the document:")

    if question:
        response = qa_chain.run(question)
        st.write(f"**Answer:** {response}")

        # Store in history
        st.session_state.chat_history.append({
            "question": question,
            "answer": response
        })

    # Show previous chat history again under main section
    if st.session_state.chat_history:
        st.write("### 🕘 Previous Conversations")
        for i, chat in enumerate(st.session_state.chat_history, 1):
            st.write(f"**Q{i}:** {chat['question']}")
            st.write(f"**A{i}:** {chat['answer']}")
'''
import streamlit as st
from utils.summarizer import summarize_text
from utils.ner import extract_entities
from utils.qa_engine import create_vector_store, create_qa_chain
from utils.file_handler import extract_text_from_file
from utils.auth import sign_up, sign_in, logout, check_login_status
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

def initialize_session_state():
    st.session_state.setdefault("chat_history", [])
    st.session_state.setdefault("new_chat", False)
    st.session_state.setdefault("logged_in", False)
    st.session_state.setdefault("username", None)
    st.session_state.setdefault("selected_model", "LLaMA")
    st.session_state.setdefault("chat_input", "")

def start_new_chat():
    st.session_state.chat_history = []
    st.session_state.new_chat = True
    st.rerun()

def handle_logout():
    logout()
    st.session_state.logged_in = False
    st.session_state.username = None
    st.rerun()

# Custom CSS to mimic ChatGPT UI
st.markdown("""
    <style>
    .main-container { max-width: 900px; margin: auto; }
    .message-user { background-color: #40414f; color: white; padding: 12px; border-radius: 10px; margin: 8px 0; }
    .message-bot { background-color: #343541; color: white; padding: 12px; border-radius: 10px; margin: 8px 0; }
    .chat-box { position: fixed; bottom: 0; width: 100%; padding: 20px 0; background: white; }
    .chat-input input { width: 80%; padding: 12px; border-radius: 6px; border: 1px solid #ccc; margin-right: 10px; }
    .chat-input button { padding: 12px 20px; background-color: #10a37f; border: none; border-radius: 6px; color: white; }
    .sidebar .block-container { padding: 1rem; }
    .sidebar-title { font-size: 18px; font-weight: bold; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

initialize_session_state()

st.markdown("<h1 style='text-align: center;'>📄 Smart Document Q&A Chatbot</h1>", unsafe_allow_html=True)

# Sidebar with profile and model selection like ChatGPT
with st.sidebar:
    if st.session_state.logged_in:
        st.markdown(f"<div class='sidebar-title'>👤 {st.session_state.username}</div>", unsafe_allow_html=True)
        if st.button("🆕 New Chat"):
            start_new_chat()
        if st.button("🚪 Logout"):
            handle_logout()

        st.markdown("<div class='sidebar-title'>🧠 Model</div>", unsafe_allow_html=True)
        selected_model = st.selectbox("Select a model:", ["LLaMA", "Bart"])
        st.session_state.selected_model = selected_model

        st.markdown("<div class='sidebar-title'>💬 Chats</div>", unsafe_allow_html=True)
        if st.session_state.chat_history:
            for i, chat in enumerate(st.session_state.chat_history, 1):
                st.markdown(f"**Q{i}:** {chat['question']}")
        else:
            st.write("No chat history yet.")
    else:
        st.markdown("### 🔐 Sign Up / Sign In")
        option = st.radio("Choose:", ["Sign Up", "Sign In"])
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if option == "Sign Up" and st.button("Sign Up"):
            sign_up(username, password)
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        elif option == "Sign In" and st.button("Sign In"):
            if sign_in(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()

st.markdown("<div class='main-container'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📎 Upload a document (TXT, PDF, DOCX)", type=["txt", "pdf", "docx"])

if uploaded_file and st.session_state.logged_in:
    file_type = uploaded_file.name.split('.')[-1].lower()
    text = extract_text_from_file(uploaded_file, file_type)

    summary = summarize_text(text)
    entities = extract_entities(text)

    st.markdown("### 📑 Document Summary")
    st.write(summary)

    vector_store = create_vector_store(text)
    qa_chain = create_qa_chain(vector_store, st.session_state.selected_model)

    st.markdown("### 💬 Chat")

    for chat in st.session_state.chat_history:
        st.markdown(f"<div class='message-user'><b>You:</b> {chat['question']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='message-bot'><b>Bot:</b> {chat['answer']}</div>", unsafe_allow_html=True)

    with st.form(key="chat_form", clear_on_submit=True):
        col1, col2 = st.columns([4, 1])
        with col1:
            question = st.text_input("", placeholder="Ask something about the document...", key="chat_input")
        with col2:
            submitted = st.form_submit_button("Send")
        if submitted and question:
            response = qa_chain.run(question)
            st.session_state.chat_history.append({"question": question, "answer": response})
            st.rerun()

    if st.session_state.chat_history:
        st.markdown("### 🕘 Previous Conversations")
        for i, chat in enumerate(st.session_state.chat_history, 1):
            st.markdown(f"**Q{i}:** {chat['question']}")
            st.markdown(f"**A{i}:** {chat['answer']}")

st.markdown("</div>", unsafe_allow_html=True)

