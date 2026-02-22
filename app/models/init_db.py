from app.database import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS section(
                   id SERIAL PRIMARY KEY,
                   section_name VARCHAR NOT NULL UNIQUE)

        """)
    conn.commit()
    

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS disease(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE)
        """)

    conn.commit()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS medication(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE)"""
    )
    conn.commit()
    
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS doctor(
                   doctor_id SERIAL PRIMARY KEY,
                   name VARCHAR(50) NOT NULL UNIQUE,
                   in_section INTEGER,
                   FOREIGN KEY (in_section) REFERENCES section(id))
            """)    
    conn.commit()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS nurs(
                   nurs_id SERIAL PRIMARY KEY,
                   name VARCHAR(50) NOT NULL UNIQUE,
                   in_section INTEGER,
                   FOREIGN KEY (in_section) REFERENCES section(id))"""
    )
    conn.commit()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS patient(
        patient_id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE,
        in_section INTEGER,
        medication INTEGER,
        FOREIGN KEY (in_section) REFERENCES section(id),
        FOREIGN KEY (medication) REFERENCES medication(id))"""
    )
    conn.commit()

    cursor.close()
    conn.close()

    print("tables are created")