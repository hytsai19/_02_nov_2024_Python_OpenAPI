
import streamlity as st

#手動建立counter_key，並設定初始值為0 (寫在dictionary中只會執行一次，稱為初始化)
if "counter" not in st.session_state:
    #st.session_state["counter"]=0
    st.session_state.counter=0

st.sessopm_state.counter +=1

st.header(f"這頁網頁已經執行"{st.session_state.copunter}次")
st.button("再執行一次", key="reset")
