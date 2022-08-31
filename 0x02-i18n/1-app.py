#!/usr/bin/env python3
"""
    Instantiate the Babel object in your app.
    Store it in a module-level variable
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
        In order to configure available languages in our app,
        you will create a Config class that has a
        LANGUAGES class attribute equal to ["en", "fr"].

        Use Config to set Babel’s default locale
        ("en") and timezone ("UTC").

        Use that class as config for your Flask app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route('/')
def index():
    """ Route to index.html """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()