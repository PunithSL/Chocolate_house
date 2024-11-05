import streamlit as st 
import datetime

from src.db_manager import add_CustomerSuggestions,get_CustomerSuggestions


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

with st.form("add_CustomerSuggestion_form"):
    customername = st.text_input("Customer Name")
    name = st.text_input("Flavor Name")
    description = st.text_area("Flavor Description")
    flavor_profile = ["Sweet","Salty","Sour","Bitter","Spicy","Fruity","Earthy"]
    
    selected_flavor = st.multiselect("Flavor",options=flavor_profile)
    flavor_profile_str = ", ".join(selected_flavor)
    main_ingredient = st.text_area("Ingredient")
    dietary_restriction = ["Vegan","Vegetarian","Gluten-Free","Dairy-Free","Nut-Free","Egg-Free","Diabetic"]

    selected_dietary = st.multiselect("Dietary Restriction",options=dietary_restriction)
        
    dietary_restriction_str = ", ".join(selected_dietary)
    allergy_concerns = ["Contains peanuts","Contains tree nuts","Contains milk","Contains lactose","Contains wheat","Contains eggs","Contains egg products","Contains sesame seeds","Contains sesame oil"]
 
    selected_allergy = st.multiselect("Allergies Concerns",options=allergy_concerns)
    allergy_concerns_str = ", ".join(selected_allergy)
    avoidance_suggestions =st.text_area("Avoidance Suggestion Description")
    submission_date = st.date_input("Submission Date",value=datetime.date.today())
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        add_CustomerSuggestions(customername,name, description, flavor_profile_str, main_ingredient, dietary_restriction_str, allergy_concerns_str, avoidance_suggestions, submission_date)
        st.success("Customer Suggestion added successfully!")


