import os
import streamlit as st
from authentication import auth, logout, cookies

def main():
    auth_page = st.Page(auth, title="Log in", icon=":material/login:")
    logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
    dashboard = st.Page(
        "analyse/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
    )

    if 'authenticated' in cookies and cookies['authenticated'] == "True":
        st.success(f"Welcome back, {cookies['email']}!")
        pg = st.navigation(
            {
                "Analyse": [dashboard],
                "Account": [logout_page]
            },
            position="sidebar",
            expanded=True
        )
    else:
        pg = st.navigation([auth_page])

    pg.run()


if __name__ == "__main__":
    main()