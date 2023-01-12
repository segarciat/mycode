#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if name__ == '__main__':
    app.run(host="0.0.0.0", port=6000)
