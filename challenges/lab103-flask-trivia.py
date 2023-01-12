import html
import pprint
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
            print(username)
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
    return questions

@app.route("/trivia", methods=["POST", "GET"])
def trivia():
    if not hasattr(request, "cookies") or request.cookies.get("username") not in users:
        return redirect(url_for("login"))
    print(f"Request method: {request.method}")
    if request.method == "GET":
        username = request.cookies.get("username")
        questions = users[username]["trivia"]
        return render_template("trivia.html", questions=questions, username=username)
    elif request.method == "POST":
        pprint.pprint(request.form)
        return "Success!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2224)
