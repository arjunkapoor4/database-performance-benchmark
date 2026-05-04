import psycopg2
import time
import csv
import os

# DB connection
conn = psycopg2.connect(
    dbname="social_db",
    user="myuser",
    password="mypassword",
    host="127.0.0.1",
    port=5433
)

cur = conn.cursor()

file_name = "postgres_results.csv"
file_exists = os.path.isfile(file_name)

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["DB", "Query", "DataSize", "Time"])

    # 1. Fetch posts
    start = time.time()

    cur.execute("SELECT * FROM posts WHERE user_id = 10")
    cur.fetchall()

    end = time.time()
    time_taken = end - start

    print("FetchPosts Time:", time_taken)
    writer.writerow(["PostgreSQL", "FetchPosts", "10K", time_taken])

    # 2. Aggregation
    start = time.time()

    cur.execute("""
        SELECT user_id, COUNT(*)
        FROM likes
        GROUP BY user_id
    """)
    cur.fetchall()

    end = time.time()
    time_taken = end - start

    print("Aggregation Time:", time_taken)
    writer.writerow(["PostgreSQL", "Aggregation", "10K", time_taken])

    # 3. Join
    start = time.time()

    cur.execute("""
        SELECT users.name, posts.content
        FROM posts
        JOIN users ON posts.user_id = users.id
    """)
    cur.fetchall()

    end = time.time()
    time_taken = end - start

    print("Join Time:", time_taken)
    writer.writerow(["PostgreSQL", "Join", "10K", time_taken])

    # 4. Top Users
    start = time.time()

    cur.execute("""
        SELECT user_id, COUNT(*) as post_count
        FROM posts
        GROUP BY user_id
        ORDER BY post_count DESC
        LIMIT 10
    """)
    cur.fetchall()

    end = time.time()
    time_taken = end - start

    print("TopUsers Time:", time_taken)

    writer.writerow(["PostgreSQL", "TopUsers", "10K", time_taken])

# cleanup
cur.close()
conn.close()

print("PostgreSQL Results saved")