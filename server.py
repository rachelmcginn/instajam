from model import Musician
from crud import create_band, create_musician
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
    return render_template('home.html')

@app.route('/create-band')
def create_band(): 
    """Creates a new band user"""
    
    
    return render_template('create-band.html')

@app.route('/handle-create-band', methods=['POST'])
def create_new_band(): 
    """Handles new band user"""
    
    email = request.form['email']
    password = request.form['password']
    display_name = request.form['display_name']
    age = request.form['age']
    gender = request.form['gender']
    influences = request.form['influences']
    location = request.form['location']
    description = request.form['description']

    user = crud.get_band_by_email(email)
    if user:
        flash("Band already exists, please log in.")
    else:
        crud.create_band(email, password, display_name, age, gender, influences, location, description)
        flash("Band successfully created!")
        return render_template("login.html")
    
    #band = request.form.get('')

    #commit to db
    
    #return render_template('dashboard.html')

# @app.route('/create-musician', methods=['GET'])
# def create_musician_user(): 
#     """Creates a new musician user"""
#     ###########
#     #new_musician = crud.create_musician()
    
#     return render_template('create-musician.html')

@app.route('/create-musician', methods=['POST'])
def create_musician_user(): 
    """Creates a new musician user"""
############
    # musician = crud.create_musician(email, password, display_name, age, gender, influences, location, description)
    #Get above values from form data 
    
    return render_template('dashboard.html')

@app.route('/sign-up')
def sign_up():
    """Displays sign up options."""
    return render_template('sign-up.html')

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


