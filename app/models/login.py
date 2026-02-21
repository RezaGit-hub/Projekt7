from app.database import get_connection

def creat_login():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS roles(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE)"""
    )

    conn.commit()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS login(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password_hash VARCHAR(60) NOT NULL,
        role_id INTEGER,
        FOREIGN KEY (role_id) REFERENCES roles(id))"""
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("login wurde erstellt")