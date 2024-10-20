import streamlit as st
from sp_client import get_sp_client

def login():
    supabase_client = get_sp_client()
    authentication_container = st.container(border=True)

    with authentication_container:
        login_tab, sign_up_tab = st.tabs(["Log in", "Sign up"])
        with login_tab:
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_password")
    
            if st.button("Log in"):
                try:
                    response = supabase_client.auth.sign_in_with_password(
                        {"email": email, "password": password}
                    )
    
                    st.session_state.user_session["expiry"] = response.session.expires_at
                    st.session_state.user_session["email"] = response.session.user.email
                    st.session_state.user_session["authenticated"] = True
                    st.toast("Successfully logged in!", icon="✅")
                    st.rerun()
                except Exception as ex:
                    st.toast(f"{ex}!", icon="⚠️")
    
        with sign_up_tab:
            email = st.text_input("Email", key="signup_email")
            password = st.text_input("Password", type="password", key="signup_password")
            
            if st.button("Sign up"):
                st.session_state.user_session = True


def logout():
    st.session_state.user_session['authenticated'] = False
    st.session_state.user_session['email'] = None
    st.session_state.user_session['expiry'] = None
    st.rerun()
