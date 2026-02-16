import psycopg2

try:
    conn = psycopg2.connect("postgresql://testuser:testpass@52.202.251.212:5432/testdb")
    cur = conn.cursor()
    
    print("Listing all tables in all schemas...")
    cur.execute("SELECT schemaname, tablename FROM pg_catalog.pg_tables WHERE schemaname NOT IN ('pg_catalog', 'information_schema');")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
