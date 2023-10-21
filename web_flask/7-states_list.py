#!/usr/bin/python3
""" Flask web application for List of states """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """
    handel teardown
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state():
    """
    display a HTML page H1 tag: “States” UL tag: with
    the list of all State objects present
    in DBStorage sorted by name (A->Z)
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
