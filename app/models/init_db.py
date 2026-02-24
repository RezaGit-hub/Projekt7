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
        """CREATE TABLE patient(
        patient_id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE,
        in_section INTEGER NOT NULL,
        medication INTEGER NOT NULL,
        CONSTRAINT fk_section FOREIGN KEY (in_section) REFERENCES section(id) ON DELETE CASCADE, 
        CONSTRAINT fk-medication FOREIGN KEY (medication) REFERENCES medication(id) ON DELETE SET NULL)"""
    )
    conn.commit()

    
    
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS patient_disease(
    patient_id INTEGER,
    disease_id INTEGER, 
    PRIMARY KEY (patient_id, disease_id),
    CONSTRAINT fk_patient FOREIGN KEY (patient_id) REFERENCES patient(patient_id) ON DELETE CASCADE,
    CONSTRAINT fk_disease FOREIGN KEY (disease_id) REFERENCES disease(id) ON DELETE CASCADE)"""
    )
    conn.commit()

    cursor.close()
    conn.close()

    print("tables are created")