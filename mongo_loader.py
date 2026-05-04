from pymongo import MongoClient
from data_generator import users, posts, likes, friends

client = MongoClient("mongodb://localhost:27017/")
db = client["social_db"]

db.users.create_index("user_id")
# clear old data
db.users.delete_many({})

print("Preparing data...")

# Pre-group posts
posts_by_user = {}
for p in posts:
    posts_by_user.setdefault(p[1], []).append({
        "post_id": p[0],
        "content": p[2]
    })

# Pre-group likes
likes_by_user = {}
for l in likes:
    likes_by_user.setdefault(l[0], []).append(l[1])

# Pre-group friends
friends_by_user = {}
for f in friends:
    friends_by_user.setdefault(f[0], []).append(f[1])

print("Inserting into MongoDB...")

documents = []

for u in users:
    documents.append({
        "user_id": u[0],
        "name": u[1],
        "posts": posts_by_user.get(u[0], []),
        "likes": likes_by_user.get(u[0], []),
        "friends": friends_by_user.get(u[0], [])
    })

# Insert in bulk (VERY FAST)
db.users.insert_many(documents)

print("MongoDB data loaded successfully")