#!/usr/bin/python3
""" Flask web application That Display Cities by states
"""
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def handel_teardown(self):
    """
    handel teardown
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def city_by_states():
    """
    Display city by state
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
