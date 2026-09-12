from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def quiz():
    result = ""
    if request.method == "POST":
        score = 0

        if request.form["q1"].lower() == "islamabad":
            score += 1
        if request.form["q2"] == "8":
            score += 1
        if request.form["q3"].lower() == "blue":
            score += 1
        if request.form["q4"].lower() == "python":
            score += 1

        result = f"Your Score: {score} out of 4"

    return f"""
    <h2>Simple Quiz App</h2>
    <form method="POST">
        Q1: What is the capital of Pakistan?<br>
        <input type="text" name="q1"><br><br>

        Q2: What is 5 + 3?<br>
        <input type="text" name="q2"><br><br>

        Q3: What is the color of the sky?<br>
        <input type="text" name="q3"><br><br>

        Q4: Which language are you learning right now?<br>
        <input type="text" name="q4"><br><br>

        <input type="submit" value="Submit Quiz">
    </form>
    <h3>{result}</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)