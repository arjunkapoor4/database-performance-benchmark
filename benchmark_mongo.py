from pymongo import MongoClient
import time
import csv
import os

# Config
DB_NAME = "social_db"
COLLECTION = "users"
CSV_FILE = "mongo_results.csv"
DATA_SIZE = "10K"   

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client[DB_NAME]
col = db[COLLECTION]

print("Connected to MongoDB")

# CSV Setup
file_exists = os.path.isfile(CSV_FILE)

with open(CSV_FILE, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["DB", "Query", "DataSize", "Time"])

    # 1. Fetch Posts (Read)
    start = time.time()

    user = col.find_one({"user_id": 10})
    posts = user["posts"]

    end = time.time()
    time_taken = end - start

    print("FetchPosts:", time_taken)
    writer.writerow(["MongoDB", "FetchPosts", DATA_SIZE, time_taken])

    # 2. Aggregation (Likes Count)
    start = time.time()

    result = col.aggregate([
        {"$unwind": "$likes"},
        {"$group": {"_id": "$user_id", "count": {"$sum": 1}}}
    ])
    list(result)

    end = time.time()
    time_taken = end - start

    print("Aggregation:", time_taken)
    writer.writerow(["MongoDB", "Aggregation", DATA_SIZE, time_taken])

    # 3. Top Users (Posts Count)
    start = time.time()

    result = col.aggregate([
        {"$project": {"post_count": {"$size": "$posts"}}},
        {"$sort": {"post_count": -1}},
        {"$limit": 10}
    ])
    list(result)

    end = time.time()
    time_taken = end - start

    print("TopUsers:", time_taken)
    writer.writerow(["MongoDB", "TopUsers", DATA_SIZE, time_taken])

    # 4. Friend Count
    start = time.time()

    result = col.aggregate([
        {"$project": {"friend_count": {"$size": "$friends"}}}
    ])
    list(result)

    end = time.time()
    time_taken = end - start

    print("FriendCount:", time_taken)
    writer.writerow(["MongoDB", "FriendCount", DATA_SIZE, time_taken])

print("MongoDB benchmark completed & saved to CSV")