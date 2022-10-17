#!/usr/bin/python3
"""script that starts a Flask web application"""


# import Flask class from flask module
from flask import Flask

# create an instance called app of the class by passong the __name__ variable
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """serves the home page

    Returns:
        str: text on the index page
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True)
