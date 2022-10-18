#!/usr/bin/python3
"""script that starts a Flask web application"""


# import Flask class from flask module
# import render_template for rendering templates to browser
# fetch data from storage engine
from flask import Flask, render_template

from models import storage

# create an instance called app of the class by passong the __name__ variable
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception=None):
    """removes the current SQLAlchemy Session
    """
    if storage is not None:
        storage.close()


@app.route('/cities_by_states')
def cities_list(n=None):
    """displays a HTML page: inside the tag BODY"""
    # check 7-states_list.py and html for another way to do this
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(debug=True)
