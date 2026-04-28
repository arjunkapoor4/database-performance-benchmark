# Performance Benchmarking of Relational, Document, and Graph Databases

## 📌 Overview
This project benchmarks and compares the performance of three types of databases:

- PostgreSQL (Relational Database)
- MongoDB (Document Database)
- Neo4j (Graph Database)

The goal is to analyze how different databases perform across various workloads such as querying, aggregation, and relationship traversal.

---

## 🎯 Objectives
- Compare performance across SQL, NoSQL, and Graph databases
- Evaluate workload-specific efficiency
- Automate benchmarking and analysis
- Visualize results using console and frontend dashboard

---

## 🛠️ Technologies Used
- Python
- PostgreSQL
- MongoDB
- Neo4j
- Flask (for frontend dashboard)
- Pandas (data processing)

# Performance Benchmarking of Relational, Document, and Graph Databases

## 📌 Overview
This project benchmarks and compares the performance of three types of databases:

- PostgreSQL (Relational Database)
- MongoDB (Document Database)
- Neo4j (Graph Database)

The goal is to analyze how different databases perform across various workloads such as querying, aggregation, and relationship traversal.

---

## 🎯 Objectives
- Compare performance across SQL, NoSQL, and Graph databases
- Evaluate workload-specific efficiency
- Automate benchmarking and analysis
- Visualize results using console and frontend dashboard

---

## 🛠️ Technologies Used
- Python
- PostgreSQL
- MongoDB
- Neo4j
- Flask (for frontend dashboard)
- Pandas (data processing)

---

## 📂 Project Structure
├── data_generator.py
├── postgres_loader.py
├── mongo_loader.py
├── neo4j_loader.py
├── benchmark_postgres.py
├── benchmark_mongo.py
├── benchmark_neo4j.py
├── run_all_analysis.py
├── app.py
├── templates/
│ └── index.html
├── postgres_results.csv
├── mongo_results.csv
├── neo4j_results.csv

---

## ⚙️ How to Run

### 1. Install dependencies

pip install pg8000 pymongo neo4j flask pandas


### 2. Start databases (Docker recommended)
- PostgreSQL → port 5432  
- MongoDB → port 27017  
- Neo4j → ports 7474 / 7687  

### 3. Load data

python postgres_loader.py
python mongo_loader.py
python neo4j_loader.py


### 4. Run benchmarking

python run_all_analysis.py


### 5. (Optional) Run frontend dashboard

python app.py


Open: http://127.0.0.1:5000

---

## 📊 Benchmark Results (Sample)

| Query Type        | Best Database |
|------------------|-------------|
| Fetch            | PostgreSQL |
| Aggregation      | PostgreSQL |
| Join             | PostgreSQL |
| Top Users        | PostgreSQL |
| Friend Count     | MongoDB |
| Mutual Friends   | Neo4j |

---

## 🧠 Key Insights
- PostgreSQL performs best for structured queries and aggregations
- MongoDB is efficient for document-based and nested data
- Neo4j excels in relationship traversal queries

---

## 🚀 Conclusion
No single database is universally optimal.  
Each database performs best depending on the workload and data model.

---

## 💼 Resume Highlight
Built an automated benchmarking system comparing PostgreSQL, MongoDB, and Neo4j across multiple workloads, demonstrating performance trade-offs and optimal database selection strategies.

---

## 📸 (Optional)
Add screenshots of:
- Console output
- Dashboard UI
- Neo4j graph visualization

---

## 👨‍💻 Author
Arjun Kapoor
---

## 📂 Project Structure
