import streamlit as st

if "key" not in st.session_state:
    st.session_state["key"]="value"
    