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


if __name__ == "__main__":
    # Run the Flask application on 0.0.0.0 interface, port 5000
    app.run(host="0.0.0.0", port=5000)
