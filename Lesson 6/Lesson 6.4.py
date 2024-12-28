import streamlit as st
import tools

sitenames:list[str]= tools.get_sitenames(excel_name="aqi.xlsx")
add_selectbox = st.sidebar.selectbox(
   " 請選擇站點名稱",
    sitenames
)
#檔名不要有空格
#run prgramme要從terminal下command: streamlit run "file_name.py"

# "with" notation

with st.sidebar:
    add_selectbox = st.selectbox(
       "請選擇站點名稱:",
        sitenames  
    )

    st.title(f"{add_selectbox}")

allData:list[dict] = tools.get_aqi(excel_name="aqi.xlsx")
#selected_item:[dict]=[]
#for item in allData:
    #if item["sitename"] == add_selectbox:
        #selected_item.append(item)

selected_item:list[dict] = [item for item in allData if item['sitename']==add_selectbox]
st.table(data=selected_item)