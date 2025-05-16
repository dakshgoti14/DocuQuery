import streamlit as st
import os
import pickle
from dotenv import load_dotenv
from google.oauth2 import id_token
from google.auth.transport.requests import Request

load_dotenv()

# File to store user data (for simplicity, storing locally in a pickle file)
USER_DATA_FILE = "user_data.pkl"

def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "rb") as f:
            return pickle.load(f)
    return {}

def save_user_data(user_data):
    with open(USER_DATA_FILE, "wb") as f:
        pickle.dump(user_data, f)

def sign_up(username, password):
    user_data = load_user_data()
    if username in user_data:
        st.error("Username already exists!")
    else:
        user_data[username] = password
        save_user_data(user_data)
        st.success("Account created successfully!")

def sign_in(username, password):
    user_data = load_user_data()
    if username not in user_data or user_data[username] != password:
        st.error("Invalid username or password!")
        return False
    return True

def logout():
    st.session_state.logged_in = False
    st.session_state.username = None

def check_login_status():
    return st.session_state.get("logged_in", False)

# Google authentication (simplified example)
def google_sign_in(google_token):
    try:
        id_info = id_token.verify_oauth2_token(google_token, Request())
        if id_info["iss"] not in ["accounts.google.com", "https://accounts.google.com"]:
            raise ValueError("Wrong issuer.")
        return id_info["email"]
    except ValueError:
        return None
