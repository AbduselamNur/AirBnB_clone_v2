#!/usr/bin/python3
from flask import Flask
""" Flask web application """


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Print Hello HBNB """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Print HBNB """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
