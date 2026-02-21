from app.database import get_connection

def inser_section(section_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO section(section_name) VALUES (%s) ON CONFLICT (section_name) DO NOTHING RETURNING id""",
                   (section_name,)
    )
    result = cursor.fetchone()
    section_id = result[0] if result else None

    conn.commit()
    cursor.close()
    conn.close()

    return section_id


def insert_doctor(name, in_section):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO doctor(name, in_section) VALUES(%s,%s) ON CONFLICT (name) DO NOTHING""",
        (name, in_section)
    )

    conn.commit()
    cursor.close()
    conn.close()

def insert_nurs(name, in_section):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO nurs(name, in_section) VALUES(%s,%s) ON CONFLICT(name) DO NOTHING""",
        (name, in_section)
    )


    conn.commit()
    cursor.close()
    conn.close()

def insert_medication(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO medication(name) VALUES(%s) ON CONFLICT(name) DO NOTHING""",
        (name,)
    )

    conn.commit()
    cursor.close()
    conn.close()

def insert_patient(name, in_section, medication_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO patient VALUES(%s,%s,%s) ON CONFLICT(name) DO NOTHING""",
        (name, in_section, medication_id)
    )

    conn.commit()
    cursor.close()
    conn.close()