import streamlit as st
from supabase import create_client


def get_supabase_client():
    """
    Create one Supabase client per Streamlit user session.
    """

    if "supabase_client" not in st.session_state:

        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_PUBLISHABLE_KEY"]

        st.session_state.supabase_client = create_client(
            url,
            key
        )

    return st.session_state.supabase_client
