from app.database import get_connection

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

