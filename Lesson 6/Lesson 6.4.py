import streamlit as st
import tools

sitenames:list[str]= tools.get_sitenames(excel_name="aqi.xlsx")
add_selectbox = st.sidebar.selectbox(
   " 請選擇站點名稱",
    sitenames
)
#檔名不要有空格
#run prgramme要從terminal下command: streamlit run "file_name.py"
