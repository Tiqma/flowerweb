import json
import mariadb

# Läs in JSON-konfigurationen
with open("data/config.json", "r") as f:
    config = json.load(f)

# Skapa connection pool
pool = mariadb.ConnectionPool(
    host=config["host"],
    user=config["user"],
    password=config["password"],
    database=config["database"],
    pool_name="mypool",
    pool_size=config.get("connectionLimit", 10)
)

def get_connection():
    """Hämta en anslutning från poolen"""
    return pool.get_connection()

# Testa anslutning vid körning
if __name__ == "__main__":
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        print("Ansluten till databasen:", db_name)
    finally:
        if 'conn' in locals() and conn:
            conn.close()