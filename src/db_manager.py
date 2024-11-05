import sqlite3
from .models import connect_db

def add_SeasonalFlavor(name,description,flavor_profile,main_ingredient,dietary_restriction,price,start_date,end_date,in_stock,rating):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO SeasonalFlavors (name,description,flavor_profile,main_ingredient,dietary_restriction,price,start_date,end_date,in_stock,rating) VALUES (?,?,?,?,?,?,?,?,?,?)
""",(name,description,flavor_profile,main_ingredient,dietary_restriction,price,start_date,end_date,in_stock,rating))
    conn.commit()
    conn.close()


def get_SeasonalFlavor():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM SeasonalFlavors
""")
    flavor = cursor.fetchall()
    conn.close()
    return flavor

def update_SeasonalFlavor(id, name,description,flavor_profile,main_ingredient,dietary_restriction,price,start_date,end_date,in_stock,rating):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE SeasonalFlavors SET name=?, description=?, flavor_profile=?, main_ingredient=?, dietary_restriction=?, price=?, start_date=?, end_date=?, in_stock=?, rating=? WHERE id=?""",( name,description,flavor_profile,main_ingredient,dietary_restriction,price,start_date,end_date,in_stock,rating,id))
    conn.commit()
    conn.close()

def delete_SeasonalFlavor(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM SeasonalFlavors WHERE id=?""",(id,))
    conn.commit()
    conn.close()

def add_Ingredients(name,quantity,unit,expiry_date,cost_per_unit,storage_condition):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Ingredients (name,quantity,unit,expiry_date,cost_per_unit,storage_condition) VALUES (?,?,?,?,?,?)
""",(name,quantity,unit,expiry_date,cost_per_unit,storage_condition))
    conn.commit()
    conn.close()

def get_Ingredients():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM Ingredients
""")
    ingredients = cursor.fetchall()
    conn.close()
    return ingredients

def update_Ingredients(id, name, quantity, unit, expiry_date, cost_per_unit, storage_condition):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Ingredients SET name=?, quantity=?, unit=?, expiry_date=?, cost_per_unit=?, storage_condition=? WHERE id=?""",(name, quantity, unit, expiry_date, cost_per_unit, storage_condition,id))
    conn.commit()
    conn.close()

def delete_Ingredients(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Ingredients WHERE id=?""",(id,))
    conn.commit()
    conn.close()

def add_CustomerSuggestions(customer_name,flavor_suggestion,flavor_description,flavor_profile,main_ingredient,dietary_restriction,allergy_concerns,avoidance_suggestions,submission_date):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO CustomerSuggestions (customer_name,flavor_suggestion,flavor_description,flavor_profile,main_ingredient,dietary_restriction,allergy_concerns,avoidance_suggestions,submission_date) VALUES (?,?,?,?,?,?,?,?,?)
""",(customer_name,flavor_suggestion,flavor_description,flavor_profile,main_ingredient,dietary_restriction,allergy_concerns,avoidance_suggestions,submission_date))
    conn.commit()
    conn.close()

def get_CustomerSuggestions():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM CustomerSuggestions
""")
    suggestions = cursor.fetchall()
    conn.close()
    return suggestions

def update_CustomerSuggestions(id, customer_name, flavor_suggestion, flavor_description, flavor_profile, main_ingredient, dietary_restriction, allergy_concerns, avoidance_suggestions, submission_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE CustomerSuggestions SET customer_name=?, flavor_suggestion=?, flavor_description=?, flavor_profile=?, main_ingredient=?, dietary_restriction=?, allergy_concerns=?, avoidance_suggestions=?, submission_date=? WHERE id=?""",( customer_name, flavor_suggestion, flavor_description, flavor_profile, main_ingredient, dietary_restriction, allergy_concerns, avoidance_suggestions, submission_date,id))
    conn.commit()
    conn.close()

def delete_CustomerSuggestions(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM CustomerSuggestions WHERE id=?""",(id,))
    conn.commit()
    conn.close()