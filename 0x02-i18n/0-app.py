#!/usr/bin/env python3
"""
    Setup a basick flask app
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """ Route to index.html"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
