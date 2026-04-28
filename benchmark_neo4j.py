from neo4j import GraphDatabase
import time
import csv
import os

# -------------------------
# Config
# -------------------------
CSV_FILE = "neo4j_results.csv"
DATA_SIZE = "10K"

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password")
)

print("Connected to Neo4j")

file_exists = os.path.isfile(CSV_FILE)

with open(CSV_FILE, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["DB", "Query", "DataSize", "Time"])

    with driver.session() as session:

        # -------------------------
        # 1. Fetch Friends
        # -------------------------
        start = time.time()

        result = session.run("""
            MATCH (u:User {id: 10})-[:FRIEND]->(f)
            RETURN f
        """)
        list(result)

        end = time.time()
        time_taken = end - start

        print("FetchFriends:", time_taken)
        writer.writerow(["Neo4j", "FetchFriends", DATA_SIZE, time_taken])

        # -------------------------
        # 2. Mutual Friends 🔥
        # -------------------------
        start = time.time()

        result = session.run("""
            MATCH (a:User {id: 10})-[:FRIEND]->(f)<-[:FRIEND]-(b:User {id: 20})
            RETURN f
        """)
        list(result)

        end = time.time()
        time_taken = end - start

        print("MutualFriends:", time_taken)
        writer.writerow(["Neo4j", "MutualFriends", DATA_SIZE, time_taken])

        # -------------------------
        # 3. Friend Count
        # -------------------------
        start = time.time()

        result = session.run("""
            MATCH (u:User)-[:FRIEND]->(f)
            RETURN u.id, COUNT(f)
        """)
        list(result)

        end = time.time()
        time_taken = end - start

        print("FriendCount:", time_taken)
        writer.writerow(["Neo4j", "FriendCount", DATA_SIZE, time_taken])

print("Neo4j benchmark completed")