import streamlit as st
st.set_page_config(page_title="Chocolate House",page_icon="❄️")

from pages.flavors import main as main_flavors
from pages.inventory import main as main_inventory
from pages.suggestions import main as main_suggestions
from pages.form_flavors import main as main_form_flavors
from pages.form_inventory import main as main_form_inventory
from pages.form_suggestions import main as main_form_suggestions


st.subheader("Chocolate House Dashboard")

form_page = st.selectbox("Select a Page",["Home","SeasonalFlavor","Inventory","Customer Suggestions","Form SeasonalFlavor","Form Inventory","Form Customer Suggestions"],key="form_page")
if(form_page =="SeasonalFlavor"):
    main_flavors()
elif(form_page =="Inventory"):
    main_inventory()
elif(form_page =="Customer Suggestions"):
    main_suggestions()
elif(form_page =="Form SeasonalFlavor"):
    main_form_flavors
elif(form_page =="Form Inventory"):
    main_form_inventory
elif(form_page =="Form Customer Suggestions"):
    main_form_suggestions()
else:
    st.write("Welcome to the Chocolate House Dashboard")
