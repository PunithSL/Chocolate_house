import streamlit as st 
import datetime

from src.db_manager import add_Ingredients,get_Ingredients,update_Ingredients,delete_Ingredients


def main():
    st.header("Ingredient Inventory")
    ingredients = get_Ingredients()
    if ingredients:
        for ingreadient in ingredients:
            st.subheader(f"{ingreadient[1]}")
            ingreadient_info ={
                "Quantity" : f"{ingreadient[2]} {ingreadient[3]}",
                "Expiry Date" : ingreadient[4],
                "Cost Per Unit" : ingreadient[5],
                "Storage Conditions" : ingreadient[6]
            }
            st.table(ingreadient_info)

            if st.button(f"Update {ingreadient[1]}"):
                with st.form("update_ingredient_form"):
                    name = st.text_input("Ingredient Name",value=ingreadient[1])
                    quantity = st.number_input("Quantity",value=ingreadient[2])
                    unit = st.selectbox("Unit",["Kg","g","L","Packet","Cans","Bunches","Slices"])
                    expiry_date = st.date_input("Expiry Date",datetime.date.today())
                    cost_per_unit = st.number_input("Cost Per Unit",value=ingreadient[5])
                    storage_conditions = ["Cool and Dry", "Refrigerated", "Frozen", "Avoid Direct Sunlight", "Keep in Airtight Container"]
                    selected_conditions = st.multiselect("Storage Conditions", options=storage_conditions,default=ingreadient[6].split(", "))

                    storage_conditions_str = ", ".join(selected_conditions)

                    submit_button = st.form_submit_button("Submit Update")
                    if submit_button:
                        update_Ingredients(ingreadient[0], name, quantity, unit, expiry_date,cost_per_unit, storage_conditions_str)
                        st.success("Ingredient updated successfully!")

            if st.button(f"Delete {ingreadient[1]}"):
                delete_Ingredients(ingreadient[0])
                st.success("Ingredient deleted successfully!")

    else:
        st.write("No Ingredients"+":smile:"*10)

if __name__ == "__main__":
    main()