from neo4j import GraphDatabase
from data_generator import users, friends

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password")
)

print("Connected to Neo4j")

def setup(tx):
    # create constraint (acts like index)
    tx.run("CREATE CONSTRAINT IF NOT EXISTS FOR (u:User) REQUIRE u.id IS UNIQUE")

def load_data(tx, users, friends):
    # create users
    tx.run("""
        UNWIND $users AS user
        MERGE (u:User {id: user.id})
        SET u.name = user.name
    """, users=[{"id": u[0], "name": u[1]} for u in users])

    # create friendships
    tx.run("""
        UNWIND $friends AS f
        MATCH (a:User {id: f.u1})
        MATCH (b:User {id: f.u2})
        MERGE (a)-[:FRIEND]->(b)
    """, friends=[{"u1": f[0], "u2": f[1]} for f in friends])

with driver.session() as session:
    print("Setting up constraints...")
    session.execute_write(setup)

    print("Loading data (users + friendships)...")
    session.execute_write(load_data, users, friends)

print("Neo4j data loaded successfully")