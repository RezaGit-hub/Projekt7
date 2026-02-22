from app.database import get_connection
from psycopg2.extras import RealDictCursor

def insert_section(section_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO section(section_name)
        VALUES (%s)
        ON CONFLICT (section_name)
        DO UPDATE SET section_name = EXCLUDED.section_name
        RETURNING id
    """, (section_name,))

    section_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return section_id

def insert_medication(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO medication(name) VALUES(%s) ON CONFLICT(name)
        DO UPDATE SET name = EXCLUDED.name
        RETURNING id""",
        (name,)
    )

    medication_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return medication_id



def insert_doctor(name, in_section):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO doctor(name, in_section) VALUES(%s,%s)
        ON CONFLICT (name) 
        DO UPDATE SET name = EXCLUDED.name
        RETURNING doctor_id""",
        (name, in_section)
    )

    doctor_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return doctor_id

def insert_nurs(name, in_section):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO nurs(name, in_section) VALUES(%s,%s) ON CONFLICT(name) 
        DO UPDATE SET name = EXCLUDED.name
        RETURNING nurs_id""",
        (name, in_section)
    )

    nurs_id = cursor.fetchone()[0]


    conn.commit()
    cursor.close()
    conn.close()

    return nurs_id


def insert_patient(name, in_section, medication):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO patient(name, in_section, medication) VALUES(%s,%s,%s) 
        ON CONFLICT(name) 
        DO UPDATE SET name = EXCLUDED.name
        RETURNING patient_id""",
        (name, in_section, medication)
    )

    patient_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return patient_id

def insert_disease(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO disease(name) VALUES(%s)
        ON CONFLICT(name)
        DO UPDATE SET name = EXCLUDED.name
        returning id""",
        (name , ) 
    )
    disease_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()
    return disease_id

def disease_to_patient(patient_id, disease_id):
    conn= get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO patient_disease(patient_id, disease_id) VALUES (%s,%s) ON CONFLICT DO NOTHING""",
        (patient_id, disease_id)
    )
    conn.commit()
    cursor.close()
    conn.close()


def get_all_doctors():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM doctor")
    doctors = cursor.fetchall()
    cursor.close()
    conn.close()

    return doctors

def get_all_section():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM section")
    sections = cursor.fetchall()
    cursor.close()
    conn.close()
    return sections

def get_all_medication():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medication")
    medications = cursor.fetchall(cursor_factory=RealDictCursor)
    cursor.close()
    conn.close()

    return medications

def get_all_patients():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM patient")
    patients = cursor.fetchall()
    cursor.close()
    conn.close()
    return patients

def get_patient_with_disease():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        """SELECT p.patient_id, p.name, d.name 
        FROM patient p JOIN patient_disease pd ON p.patient_id = pd.patient_id
        JOIN disease d on pd.disease_id = d.id"""
    )

    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result