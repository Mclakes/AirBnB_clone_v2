#!/usr/bin/python3
"""
Module for a Flask web application
"""
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define a route for the root URL '/' with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Function to display the message "Hello HBNB!" when the root URL is accessed
    """
    return "Hello HBNB!"


# Define a route for the '/hbnb' URL with strict_slashes=False
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Function to display the message "HBNB" when the '/hbnb' URL is accessed
    """
    return "HBNB"


# Define a route for the '/c/<text>' URL with strict_slashes=False
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Function to display the message "C " followed by the value of the text
    variable (replace underscore _ symbols with a space)
    """
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    # Run the Flask application on 0.0.0.0 interface, port 5000
    app.run(host="0.0.0.0", port=5000)
