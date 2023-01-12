#!/usr/bin/env python3

from flask import (
    Flask, 
    render_template, 
    request,
    make_response,
    redirect,
    url_for
)

EXPECTED = 4

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/math", methods=["POST"])
def math():
    answers = {
        "name": request.form.get("name"),
        "addition": int(request.form.get("addition"))
    }

    response = make_response(render_template("math.html", **answers))
    response.set_cookie("name", answers.get("name"))
    response.set_cookie("wizard", str(answers.get("addition") == EXPECTED))

    return response

@app.route("/hogwarts")
def hogwarts():
    name = request.cookies.get("name", None)
    is_wizard = request.cookies.get("wizard")

    if is_wizard == "True":
        return f"<h1>You're a wizard, {name}</h1>"
    else:
        message = f"<h1>{name}? Not on the list.</h1>"
        return message


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)
