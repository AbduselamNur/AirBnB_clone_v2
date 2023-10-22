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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_with_id(id=None):
    """ Display state/ID """
    states = storage.all(State)
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', states=states, state_id=id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
