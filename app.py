import streamlit as st
from pages import flavors

st.sidebar.title("Chocolate House Dashboard")

page = st.sidebar.select_slider("Select a Page",["Home","SeasonalFlavor"])
if(page =="SeasonalFlavor"):
    flavors
else:
    st.write("Welcome to the Chocolate House Dashboard")