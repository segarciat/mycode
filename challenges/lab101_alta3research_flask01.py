#!/usr/bin/env python3

from flask import Flask, render_template, request

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
    print(answers)

    return render_template("math.html", **answers)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)
