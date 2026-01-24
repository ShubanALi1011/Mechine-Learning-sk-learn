import streamlit as st

# --- Dummy credentials ---
USERNAME = "admin"
PASSWORD = "1234"

# --- Title ---
st.title("Dummy Login Page")

# --- Input fields ---
username_input = st.text_input("Username")
password_input = st.text_input("Password", type="password")

# --- Login button ---
if st.button("Login"):
    if username_input == USERNAME and password_input == PASSWORD:
        st.success(f"Welcome {username_input}!")
        st.write("You are now logged in ✅")
        # --- Place your app content below ---
        st.write("This is your main app content...")
    else:
        st.error("Incorrect username or password ❌")
