import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME")
)



def test_connection():
    try:
        conn =  get_connection()

        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        print("Database connection successful ")

        cursor.close()
        conn.close()

    except Exception as e:
        print("Connection failed ")
        print(e)

if __name__ == "__main__":
    test_connection()

