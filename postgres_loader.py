import psycopg2
from data_generator import users, posts, likes, friends

print("Trying to connect...")

conn = psycopg2.connect(
    dbname="social_db",
    user="myuser",
    password="mypassword",
    host="127.0.0.1",
    port="5432"
)
cur = conn.cursor()
print("Connected to PostgreSQL")

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        content TEXT
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS likes (
        user_id INTEGER,
        post_id INTEGER REFERENCES posts(id)
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS friends (
        user_id INTEGER,
        friend_id INTEGER
    );
""")

conn.commit()
print("Tables created")

cur.executemany("INSERT INTO users VALUES (%s, %s)", users)
print("Inserted users")

cur.executemany("INSERT INTO posts VALUES (%s, %s, %s)", posts)
print("Inserted posts")

cur.executemany("INSERT INTO likes VALUES (%s, %s)", likes)
print("Inserted likes")

cur.executemany("INSERT INTO friends VALUES (%s, %s)", friends)
print("Inserted friends")

conn.commit()
cur.close()
conn.close()
print("Done")