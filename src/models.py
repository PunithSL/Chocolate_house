import sqlite3

def connect_db():
    return sqlite3.connect("database.db")

def create_tables():
    try:
        conn = connect_db()
        cursor = conn.cursor()


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS SeasonalFlavors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    description TEXT NOT NULL,
                    flavor_profile TEXT NOT NULL,
                    main_ingredient TEXT NOT NULL,
                    dietary_restriction TEXT,
                    price REAL NOT NULL,
                    start_date DATE,
                    end_date DATE,
                    in_stock BOOLEAN NOT NULL,
                    rating REAL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Ingredients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    quantity REAL,
                    unit TEXT NOT NULL,
                    expiry_date DATE,
                    cost_per_unit REAL,
                    storage_condition TEXT
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS CustomerSuggestions  (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT,
                    flavor_suggestion UNIQUE TEXT<
                    flavor_description TEXT,
                    flavor_profile TEXT NOT NULL,
                    main_ingredient TEXT NOT NULL,
                    dietary_restriction TEXT,
                    allergy_concerns TEXT,
                    avoidance_suggestions TEXT,
                    submission_date DATE
            );
        """)
    except:
        print("An error occurred while creating tables.")
    else:
        conn.commit()
        conn.close()
    

create_tables()
print("DataBase Tables Created SuccessFully")