import streamlit as st
from sp_client import get_sp_client
from streamlit_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(
    prefix=st.secrets.cookies.prefix,
    password=st.secrets.cookies.password,
)

if not cookies.ready():
    st.stop()

def store_authentication_cookies(cookies, response):
    cookies["expiry"] = str(response.session.expires_at)
    cookies["email"] = response.session.user.email
    cookies["authenticated"] = "True"
    cookies.save()

def login():
    supabase_client = get_sp_client()
    authentication_container = st.container(border=True, key='auth_container')

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

                    if response:
                        store_authentication_cookies(cookies, response)
                        st.rerun()
                    else:
                        raise Exception("Failed to retrieve credentials")
                except Exception as ex:
                    st.toast(f"{ex}!", icon="⚠️")

        with sign_up_tab:
            email = st.text_input("Email", key="signup_email")
            password = st.text_input("Password", type="password", key="signup_password")

            if st.button("Sign up"):
                st.session_state.user_session = True

def logout():
    cookies['authenticated'] = "False"
    del cookies['email']
    del cookies['expiry']
    st.rerun()
