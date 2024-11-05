import streamlit as st 
import datetime

from src.db_manager import add_Ingredients,get_Ingredients


st.header("Ingredient Inventory")
ingredients = get_Ingredients()
if ingredients:
    for ingreadient in ingredients:
        st.subheader(f"{ingreadient[1]}")
        ingreadient_info ={
            "Quality" : f"{ingreadient[2]} {ingreadient[3]}",
            "Expiry Date" : ingreadient[4],
            "Cost Per Unit" : ingreadient[5],
            "Storage Conditions" : ingreadient[6]
        }
        st.table(ingreadient_info)

with st.form("add_IngredientInventory_form"):
    name = st.text_input("Ingredient Name")
    quantity = st.number_input("Quantity")
    unit = st.selectbox("Unit",["Kg","g","L","Packet","Cans","Bunches","Slices"])
    expiry_date = st.date_input("Expiry Date",datetime.date(2024,11,5))
    cost_per_unit = st.number_input("Cost Per Unit")
    storage_conditions = ["Cool and Dry", "Refrigerated", "Frozen", "Avoid Direct Sunlight", "Keep in Airtight Container"]
    selected_conditions = st.multiselect("Storage Conditions", options=storage_conditions)

    storage_conditions_str = ", ".join(selected_conditions)
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        add_Ingredients(name, quantity, unit, expiry_date, cost_per_unit, storage_conditions_str)
        st.success("Ingredients added successfully!")

