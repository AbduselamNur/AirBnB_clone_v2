#!/usr/bin/python3
""" Flask web application """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Print Hello HBNB!"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Print HBNB """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Print C By Replace '_' to ' ' """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ Print Python is cool/text """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def n(n):
    """  display “n is a number” only if n is an integer """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
