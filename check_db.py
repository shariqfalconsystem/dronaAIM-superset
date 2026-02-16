import psycopg2
import sys

try:
    conn = psycopg2.connect("postgresql://testuser:testpass@52.202.251.212:5432/testdb")
    cur = conn.cursor()
    
    print("Checking active queries...")
    cur.execute("SELECT pid, state, query, wait_event_type, wait_event FROM pg_stat_activity WHERE state != 'idle';")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    print("\nChecking table size for tagged_object...")
    cur.execute("SELECT count(*) FROM tagged_object;")
    count = cur.fetchone()[0]
    print(f"Row count in tagged_object: {count}")
    
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
