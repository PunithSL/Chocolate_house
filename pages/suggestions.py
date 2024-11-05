import streamlit as st 
import datetime

from src.db_manager import add_CustomerSuggestions,get_CustomerSuggestions,update_CustomerSuggestions,delete_CustomerSuggestions

def main():
    st.header("Seasonal Flavors")
    suggestions = get_CustomerSuggestions()
    if suggestions:
        for suggestion in suggestions:
            st.subheader(f"Customer Name :{suggestion[1]} \nFlavore : {suggestion[2]}")
            st.markdown(f"Description : {suggestion[3]}")
            suggestion_info ={
                "Flavore Profile" : suggestion[4],
                "Ingredient Profile" : suggestion[5],
                "Dietary Restrictions" : suggestion[6],
                "Allergy Concern" : suggestion[7],
                "Avoidance Suggestions" : suggestion[8],
                "Submission Date " : suggestion[9]
            }
            st.table(suggestion_info)

            if st.button(f"Update {suggestion[1]}"):
                with st.form("update_suggestion_form"):
                    customername = st.text_input("Customer Name", value=suggestion[1])
                    name = st.text_input("Flavor Name", value=suggestion[2])
                    description = st.text_area("Description", value=suggestion[3])

                    flavor_profile = ["Sweet", "Salty", "Sour", "Bitter", "Spicy", "Fruity", "Earthy"]
                    selected_flavor = st.multiselect("Flavor Profile", options=flavor_profile, default=suggestion[4].split(", "))
                    flavor_profile_str = ", ".join(selected_flavor)

                    main_ingredient = st.text_area("Ingredient", value=suggestion[5])

                    dietary_restriction = ["Vegan", "Vegetarian", "Gluten-Free", "Dairy-Free", "Nut-Free", "Egg-Free", "Diabetic"]
                    selected_dietary = st.multiselect("Dietary Restriction", options=dietary_restriction, default=suggestion[6].split(", "))
                    dietary_restriction_str = ", ".join(selected_dietary)
                    allergy_concerns = ["Contains peanuts","Contains tree nuts","Contains milk","Contains lactose","Contains wheat","Contains eggs","Contains egg products","Contains sesame seeds","Contains sesame oil"]
                    selected_allergy = st.multiselect("Allergies Concerns",options=allergy_concerns,default=suggestion[7].split(", "))
                    allergy_concerns_str = ", ".join(selected_allergy)
                    avoidance_suggestions =st.text_area("Avoidance Suggestion Description", value=suggestion[8])
                    submission_date = st.date_input("Submission Date",datetime.date.today())
                    submit_button = st.form_submit_button("Submit Update")

                    if submit_button:
                        update_CustomerSuggestions(
                            suggestion[0],customername, name, description, flavor_profile_str, main_ingredient,
                            dietary_restriction_str, allergy_concerns_str, avoidance_suggestions, submission_date
                        )
                        st.success("Suggestion updated successfully!")

            if st.button(f"Delete {suggestion[1]}"):
                delete_CustomerSuggestions(suggestion[0])
                st.success("Suggestions deleted successfully!")


    else:
        st.write("No Suggestions"+":smile:"*10)

if __name__ == "__main__":
    main()