from faker import Faker
import random

fake = Faker()

NUM_USERS = 10000  # start small

users = []
posts = []
likes = []
friends = []

post_id = 1

for i in range(NUM_USERS):
    # create user
    users.append((i, fake.name()))

    # create posts for each user
    for _ in range(random.randint(1, 3)):
        posts.append((post_id, i, fake.text()))

        # likes on post
        for _ in range(random.randint(1, 5)):
            likes.append((random.randint(0, NUM_USERS-1), post_id))

        post_id += 1

    # create friends
    for _ in range(3):
        friends.append((i, random.randint(0, NUM_USERS-1)))

print("Generated:",
      len(users), "users,",
      len(posts), "posts")