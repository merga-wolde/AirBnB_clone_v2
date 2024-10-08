#!/usr/bin/python3
"""
file: 0-hello_route.py
desc: This module runs a simple

"""
from flask import Flask

app = Flask(__name__)

@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB! from the root path"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
