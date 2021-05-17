from Instajam.model import Musician
from Instajam.crud import create_band, create_musician
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

@app.route('/create-account')
def create_account(user_type):
    """Creates a new account"""
    # if user_type == "band":
    #     create_band()
    # if user_type == "musician":
    #     create_musician() ########Not sure if this should be here or in crud
    return render_template('create-account.html')

@app.route('/login')
def login():
    """Logs in existing user"""
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """Displays dashboard to logged in user"""
    return render_template('dashboard.html')

# @app.route('/user-profile')
# def user_profile():
#     """Displays the profile of currently logged in user"""
#     return render_template('user-profile.html')

@app.route('/match-queue')
def jam_queue():
    """View potential matches"""
    return render_template('match-queue.html')

@app.route('/matches')
def matches():
    """Displays profiles the user has matched with"""
    return render_template('matches.html')

#Should these be 2 view functions or can it be condensed into one?
@app.route('/users/<musician_id>') ###
def musician_profile(musician_id):
    """View a musician's profile"""

    musician = crud.get_musician_by_id(musician_id)

    return render_template('user_profile.html', musician=musician_id)

@app.route('/users/<band_id>')  ###
def band_profile(band_id):
    """View a band's profile"""

    band = crud.get_band_by_id(band_id)

    return render_template('user_profile.html', band=band_id)

###Contact match###




if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')


