from .import taipei
import streamlit as st

@st.dialog("Cast your vote)
def vote(item):
    st.write(error)

try:
    youbike_data:list[dict] = taipei.get_youbikes()
except Exception as e:
    print(e)
    st.stop
else:
    print(youbike_data)

