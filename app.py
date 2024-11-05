import streamlit as st
st.set_page_config(page_title="Chocolate House",page_icon="❄️")
from pages import flavors,inventory,suggestions



st.subheader("Chocolate House Dashboard")

page = st.select_slider("Select a Page",["Home","SeasonalFlavor","Inventory","Customer Suggestions"])
if(page =="SeasonalFlavor"):
    flavors
elif(page =="Inventory"):
    inventory
elif(page =="Customer Suggestions"):
    suggestions
else:
    st.write("Welcome to the Chocolate House Dashboard")