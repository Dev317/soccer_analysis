import os
import streamlit as st
from authentication import login, logout

def main():
    if "user_session" not in st.session_state:
        st.session_state.user_session = {
            "authenticated": False
        }

    login_page = st.Page(login, title="Log in", icon=":material/login:")
    logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
    dashboard = st.Page(
        "analyse/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
    )

    if st.session_state.user_session['authenticated']:
        pg = st.navigation(
            {
                "Analyse": [dashboard],
                "Account": [logout_page]
            },
            position="sidebar",
            expanded=True
        )
    else:
        pg = st.navigation([login_page])

    pg.run()


if __name__ == "__main__":
    main()