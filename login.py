import streamlit as st
from firebase_admin import auth
from firebase_init import initialize_firebase

initialize_firebase()  # Ensure Firebase is initialized

def register_user(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        st.success(f"Successfully registered user: {user.email}")
    except Exception as e:
        st.error(f"Error creating user: {e}")

def login_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        st.success(f"Successfully logged in user: {user.email}")
    except auth.AuthError as e:
        st.error(f"Error logging in: {e.message}")
    except Exception as e:
        st.error(f"Error logging in: {e}")

def main():
    st.title("PollVue")
    st.subheader("Register New User")

    reg_email = st.text_input("Email for Registration")
    reg_password = st.text_input("Password for Registration", type="password")
    register_button = st.button("Register")

    if register_button:
        register_user(reg_email, reg_password)

    st.subheader("Login")
    login_email = st.text_input("Email for Login")
    login_password = st.text_input("Password for Login", type="password")
    login_button = st.button("Login")

    if login_button:
        login_user(login_email, login_password)

if __name__ == "__main__":
    main()
