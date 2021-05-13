from flask import (Flask, render_template, request, flash, session, redirect)

import crud
from model import connect_to_db
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage"""
    return render_template('homepage.html')

@app.route('/jam-queue')
def jam_queue():
    """View other users available to match with"""
    return render_template('jam-queue.html')

@app.route('/matches')
def matches():
    """Displays profiles the user has matched with"""
    return render_template('matches.html')

@app.route('/user-profile')
def user_profile():
    """Displays the profile of currently logged in user"""
    return render_template('user-profile.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')


