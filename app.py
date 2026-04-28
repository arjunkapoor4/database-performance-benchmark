from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # load all results
    df1 = pd.read_csv("postgres_results.csv")
    df2 = pd.read_csv("mongo_results.csv")
    df3 = pd.read_csv("neo4j_results.csv")

    df = pd.concat([df1, df2, df3])

    # convert to dict for frontend
    data = df.to_dict(orient="records")

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)