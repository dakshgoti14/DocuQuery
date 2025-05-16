import streamlit as st

def init_session():
    if "history" not in st.session_state:
        st.session_state.history = []
    if "doc_texts" not in st.session_state:
        st.session_state.doc_texts = {}
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = None
