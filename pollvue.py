import streamlit as st
import dashboard
import new
import login
import my_nltk_script
from firebase_init import initialize_firebase  # Ensure Firebase is initialized

# Main page layout
st.set_page_config(page_title="PollVue", layout="wide")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Home", "Dashboard", "Login/Signup", "Statistics"])

# Display selected page
if page == "Home":
    new.main()
elif page == "Dashboard":
    dashboard.main()
elif page == "Login/Signup":
    login.main()
elif page == "Statistics":
    my_nltk_script.main()