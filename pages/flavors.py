import streamlit as st 
import datetime

from src.db_manager import add_SeasonalFlavor,get_SeasonalFlavor,update_SeasonalFlavor,delete_SeasonalFlavor


def main():

    st.header("Seasonal Flavors")
    flavors = get_SeasonalFlavor()
    if flavors:
        for flavor in flavors:
            st.subheader(f"{flavor[1]}")
            st.markdown(f"Description : {flavor[2]}")
            flavor_info ={
                "Flavor Profile" : flavor[3],
                "Ingredient Profile" : flavor[4],
                "Dietary Restrictions" : flavor[5],
                "Price" : flavor[6],
                "Start Date" : flavor[7],
                "End Date" : flavor[8],
                "In Stock" : flavor[9],
                "Rating" : flavor[10]
            }
            st.table(flavor_info)

            if st.button(f"Update {flavor[1]}"):
                with st.form("update_flavor_form"):
                    name = st.text_input("Flavor Name", value=flavor[1])
                    description = st.text_area("Description", value=flavor[2])

                    flavor_profile = ["Sweet", "Salty", "Sour", "Bitter", "Spicy", "Fruity", "Earthy"]
                    selected_flavor = st.multiselect("Flavor Profile", options=flavor_profile, default=flavor[3].split(", "))
                    flavor_profile_str = ", ".join(selected_flavor)

                    main_ingredient = st.text_area("Ingredient", value=flavor[4])

                    dietary_restriction = ["Vegan", "Vegetarian", "Gluten-Free", "Dairy-Free", "Nut-Free", "Egg-Free", "Diabetic"]
                    selected_dietary = st.multiselect("Dietary Restriction", options=dietary_restriction, default=flavor[5].split(", "))
                    dietary_restriction_str = ", ".join(selected_dietary)

                    price = st.select_slider("Price", options=range(1, 501), value=flavor[6])
                    start_date = st.date_input("Start Date of Seasonal Flavors", datetime.date.today())
                    end_date = st.date_input("End Date of Seasonal Flavors", datetime.date.today())

                    in_stock = st.radio("In Stock", ['Yes', 'No'], index=0 if flavor[9] == 'Yes' else 1)
                    rating = st.select_slider("Ratings", options=range(1, 6), value=flavor[10])

                    submit_button = st.form_submit_button("Submit Update")
                    if submit_button:
                        update_SeasonalFlavor(flavor[0], name, description, flavor_profile_str, main_ingredient,dietary_restriction_str, price, start_date, end_date, in_stock, rating)
                        st.success("Flavor updated successfully!")

            if st.button(f"Delete {flavor[1]}"):
                delete_SeasonalFlavor(flavor[0])
                st.success("Flavor deleted successfully!")

    else:
        st.write("No Flavors"+":smile:"*10)

if __name__ == "__main__":
    main()