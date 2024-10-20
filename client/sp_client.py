import streamlit as st
from supabase import create_client, Client

def get_sp_client():
    url = st.secrets.supabase.url
    key = st.secrets.supabase.key
    return create_client(url, key)
