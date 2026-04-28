import os
import subprocess
import sys
import pandas as pd
from collections import defaultdict

# -------------------------
# Step 1: Clear old CSVs
# -------------------------
files = ["postgres_results.csv", "mongo_results.csv", "neo4j_results.csv"]

for file in files:
    if os.path.exists(file):
        os.remove(file)

print("\n🧹 Old CSV files cleared\n")

# -------------------------
# Step 2: Run benchmarks
# -------------------------
print("🚀 Running PostgreSQL benchmark...")
subprocess.run([sys.executable, "benchmark_postgres.py"])

print("\n🚀 Running MongoDB benchmark...")
subprocess.run([sys.executable, "benchmark_mongo.py"])

print("\n🚀 Running Neo4j benchmark...")
subprocess.run([sys.executable, "benchmark_neo4j.py"])

# -------------------------
# Step 3: Load data
# -------------------------
dfs = []

if os.path.exists("postgres_results.csv"):
    dfs.append(pd.read_csv("postgres_results.csv"))

if os.path.exists("mongo_results.csv"):
    dfs.append(pd.read_csv("mongo_results.csv"))

if os.path.exists("neo4j_results.csv"):
    dfs.append(pd.read_csv("neo4j_results.csv"))

if not dfs:
    print("❌ No data found. Benchmarks failed.")
    exit()

df = pd.concat(dfs, ignore_index=True)

# -------------------------
# Step 4: Clean Table Output
# -------------------------
print("\n================ DATABASE PERFORMANCE =================\n")

print(f"{'DB':<12} | {'Query':<15} | {'Time (s)':<10}")
print("-" * 45)

for _, row in df.iterrows():
    print(f"{row['DB']:<12} | {row['Query']:<15} | {row['Time']:<10.4f}")

# -------------------------
# Step 5: Query-wise Ranking
# -------------------------
print("\n📊 QUERY-WISE RANKING\n")

grouped = defaultdict(list)

for _, row in df.iterrows():
    grouped[row["Query"]].append((row["DB"], row["Time"]))

for query, values in grouped.items():
    sorted_vals = sorted(values, key=lambda x: x[1])

    print(f"🔹 {query}")
    for i, (db, t) in enumerate(sorted_vals, 1):
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉"
        print(f"   {medal} {db:<10} → {t:.4f}s")
    print()

# -------------------------
# Step 6: Overall Ranking
# -------------------------
print("🏆 OVERALL RANKING\n")

avg_times = df.groupby("DB")["Time"].mean().sort_values()

for i, (db, t) in enumerate(avg_times.items(), 1):
    medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉"
    print(f"{medal} {db:<12} → Avg: {t:.4f}s")

# -------------------------
# Step 7: Final Insights
# -------------------------
print("\n💡 FINAL INSIGHTS\n")

print("✔ PostgreSQL excels in structured queries & aggregation")
print("✔ MongoDB performs well for flexible document-based data")
print("✔ Neo4j dominates relationship-based queries (Mutual Friends)\n")

print("======================================================\n")