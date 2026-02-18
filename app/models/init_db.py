from app.database import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS section(
                   id SERIAL PRIMARY KEY,
                   section_name VARCHAR NOT NULL)

        """)
    conn.commit()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS roles(
                   id SERIAL PRIMARY KEY,
                   role_name VARCHAR(40) NOT NULL UNIQUE,
                   section_id INTEGER ,
                   FOREIGN KEY (section_id) REFERENCES section(id))
                   
                   """)
    conn.commit()
    
    
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS doctor(
                   doctor_id SERIAL PRIMARY KEY,
                   name VARCHAR(50) NOT NULL UNIQUE,
                   in_section INTEGER,
                   role_id INTEGER,
                   FOREIGN KEY (in_section) REFERENCES section(id),
                   FOREIGN KEY (role_id) REFERENCES roles(id) )
            """)
    
    conn.commit()
    cursor.close()
    conn.close()

    print("tables are created")