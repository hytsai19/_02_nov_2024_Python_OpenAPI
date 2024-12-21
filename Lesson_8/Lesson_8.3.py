from tools import fetch_youbike_data
import streamlit as st

youbike_data:list[dict]=fetch_youbike_data()

#分兩個欄位
#使用youbike_data:list的資料, 取出所有的行政區域(sarea),不可以重複
#右邊是選擇"行政區域(sarea)",使用下拉式表單
#左邊是選擇該行政區域的YouBike站點資訊
#最下方是該行政區域的YouBike站點資料的地圖


