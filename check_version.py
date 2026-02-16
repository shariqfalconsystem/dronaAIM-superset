import psycopg2

try:
    conn = psycopg2.connect("postgresql://testuser:testpass@52.202.251.212:5432/testdb")
    cur = conn.cursor()
    
    print("Checking alembic_version...")
    cur.execute("SELECT * FROM alembic_version;")
    row = cur.fetchone()
    print(f"Current version in DB: {row}")
    
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
