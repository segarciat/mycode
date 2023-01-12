import html
import crayons
import random
from flask import (
    Flask,
    redirect,
    request,
    url_for,
    render_template,
    make_response
)

import requests

TRIVIA_URL = "https://opentdb.com/api.php?amount=10"

app = Flask(__name__)
users = dict()

@app.route("/")
def index():
    username = request.cookies.get("username")
    if username in users:
        return redirect(url_for("trivia"))
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", username='')
    elif request.method == "POST":
        username = request.form.get("username")
        if username in users:
            return render_template("login.html", username=username)
        else:
            response = make_response(redirect(url_for("trivia")))
            users[username] = {"trivia": make_trivia()}
            response.set_cookie("username", username)
            return response

def make_trivia():
    # Get questions from a different API
    trivia_api_response = requests.get(TRIVIA_URL)
    trivia_data = trivia_api_response.json()
    questions = trivia_data["results"]
    for question in questions:
        question["question"] = html.unescape(question["question"])
        question["choices"] = [html.unescape(choice) for choice in [
            question["correct_answer"], *question["incorrect_answers"]]
        ]
        random.shuffle(question["choices"])
    return questions

@app.route("/trivia", methods=["POST", "GET"])
def trivia():
    if not hasattr(request, "cookies") or request.cookies.get("username") not in users:
        return redirect(url_for("login"))
    username = request.cookies.get("username")
    questions = users[username]["trivia"]
    if request.method == "GET":
        return render_template("trivia.html", questions=questions, username=username)
    elif request.method == "POST":
        score = 0
        for q in questions:
            question = q["question"]
            correct_answer = q["correct_answer"]
            user_answer = request.form.get(question)
            if user_answer == correct_answer:
                score += 1
        return f"<h1>{username}, you got {score} questions correct out of {len(questions)}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2224)
