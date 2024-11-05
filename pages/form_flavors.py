import streamlit as st 
import datetime

from src.db_manager import add_SeasonalFlavor,get_SeasonalFlavor

def main():
    with st.form("add_SeasonalFlavor_form"):
        name = st.text_input("Flavor Name")
        description = st.text_area("Description")
        flavor_profile = ["Sweet","Salty","Sour","Bitter","Spicy","Fruity","Earthy"]
        selected_flavor = st.multiselect("Flavor",options=flavor_profile)

        flavor_profile_str = ", ".join(selected_flavor)
        main_ingredient = st.text_area("Ingredient")
        dietary_restriction = ["Vegan","Vegetarian","Gluten-Free","Dairy-Free","Nut-Free","Egg-Free","Diabetic"]
        selected_dietary = st.multiselect("Dietary Restriction",options=dietary_restriction)

        dietary_restriction_str = ", ".join(selected_dietary)
        price = st.select_slider("Price",options=range(1,501),value=100)
        start_date = st.date_input("Start Date of Seasonal Flavors",datetime.date(2024,11,5))
        end_date = st.date_input("End Date of Seasonal Flavors", datetime.date(2024,11,15))
        in_stock = st.radio("In Stock",['Yes','No'])
        rating=st.select_slider("Ratings",options=range(1,6),value=3)
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            add_SeasonalFlavor(name, description, flavor_profile_str, main_ingredient, dietary_restriction_str, price, start_date, end_date, in_stock, rating)
            st.success("Flavor added successfully!")
            flavors = get_SeasonalFlavor()

if __name__ == "__main__":
    main()