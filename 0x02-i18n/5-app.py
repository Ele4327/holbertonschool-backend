#!/usr/bin/env python3
"""
    Instantiate the Babel object in your app.
    Store it in a module-level variable
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union
from os import getenv

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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


app.config.from_object('5-app.Config')


@app.route('/')
def index():
    """ Route to index.html """
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """
        Function with the babel.localeselector decorator.
        Use request.accept_languages to determine
        the best match with our supported languages.
    """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user() -> Union[dict, None]:
    """
        Returns a user dictionary, or none if the ID cannot be found,
        or if login_as was not passed.
    """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None

@app.before_request
def before_request():
    """
        Should use get_user to find a user if any,
        and set it as a global on flask.g.user
    """
    g.user = get_user()

if __name__ == "__main__":
    app.run(debug=True)
