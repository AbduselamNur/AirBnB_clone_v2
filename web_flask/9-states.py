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


@app.route("/states", strict_slashes=False)
def city_by_states():
    """
    Display state
    """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, mode="all")


@app.route("/states/<id>")
def state_id(id):
    """
    Display State By ID
    """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=id, mode="one")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
