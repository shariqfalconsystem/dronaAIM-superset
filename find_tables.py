import psycopg2

try:
    conn = psycopg2.connect("postgresql://testuser:testpass@52.202.251.212:5432/testdb")
    cur = conn.cursor()
    
    print("Searching for specific tables...")
    cur.execute("""
        SELECT schemaname, tablename 
        FROM pg_catalog.pg_tables 
        WHERE tablename IN ('alembic_version', 'tagged_object', 'tag', 'dashboards', 'slices');
    """)
    rows = cur.fetchall()
    if not rows:
        print("No matching tables found in any schema.")
    for row in rows:
        print(row)
        
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
