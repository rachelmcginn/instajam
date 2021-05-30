from model import Musician
from crud import create_band, create_musician
from flask import (Flask, render_template, request, flash, session, redirect)

import crud
from model import connect_to_db
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/set-session')
def set_session():
    """Sets session info for currently logged in user"""

    user_type = session.get('user_type')
    user_id = session.get('user_id')
    
    session['user_id'] = user_id
    session['user_type'] = user_type

    return redirect ('display-session.html')


@app.route('/display-session')
def display_session():
    """Displays session info for currently logged in user"""

    print(session)

    return render_template('display-session.html')


@app.route('/')
def homepage():
    """View homepage"""
    return render_template('home.html')


@app.route('/create-band')
def create_band(): 
    """Displays form to create a new band user"""
    
    
    return render_template('create-band.html')


@app.route('/handle-create-band', methods=['POST'])
def handle_create_band(): 
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
        flash("Band profile successfully created!")
        return render_template("login.html")


@app.route('/create-musician')
def create_musician(): 
    """Displays form to create a new musician user"""
    
    
    return render_template('create-musician.html')


@app.route('/handle-create-musician', methods=['POST'])
def handle_create_musician(): 
    """Handles new musician user"""
    
    email = request.form['email']
    password = request.form['password']
    display_name = request.form['display_name']
    age = request.form['age']
    gender = request.form['gender']
    influences = request.form['influences']
    location = request.form['location']
    description = request.form['description']

    user = crud.get_musician_by_email(email)
    if user:
        flash("Musician already exists, please log in.")
    else:
        crud.create_musician(email, password, display_name, age, gender, influences, location, description)
        flash("Musician profile successfully created!")
        return render_template("login.html")


@app.route('/sign-up')
def sign_up():
    """Displays sign up options."""
    return render_template('sign-up.html')


@app.route('/login')
def login():
    """Log in"""
    return render_template('login.html')


@app.route('/handle-login-band', methods = ['POST'])
def handle_login_band():
    """Handles log in for band user"""

    email = request.form['email']
    password = request.form['password']
    
    user = crud.get_band_by_email(email)

    if user == None:
        flash('Account does not exist. Please try again.')
        return redirect ('/')
    else:
        if (password == user.password):
            session['user_type'] = 'band' 
            session['user_id'] = user.band_id 
            
            flash(f'Logged in as {email}')
            return redirect ('/dashboard')  
        else:
            flash('Incorrect Password. Please try again.')
            return redirect ('/')  


@app.route('/handle-login-musician', methods = ['POST'])
def handle_login_musician():
    """Handles log in for musician user"""

    email = request.form['email']
    password = request.form['password']
    
    user = crud.get_musician_by_email(email)

    if user == None:
        flash('Account does not exist. Please try again.')
        return redirect ('/')
    else:
        if (password == user.password):
            session['user_type'] = 'musician' 
            session['user_id'] = user.musician_id 
            
            flash(f'Logged in as {email}')
            return redirect ('/dashboard')  
        else:
            flash('Incorrect Password. Please try again.')
            return redirect ('/')  


@app.route('/dashboard')
def dashboard():
    """Displays dashboard to logged in user"""
    #Want to add "hello [displayname] via jinja"

    user_type = session.get('user_type')
    #dn = "hello" #can't pass to jinja 

    if user_type == None:
        return  redirect ('/login')
    if user_type == 'band':
        return render_template('dashboard.html') 
    if user_type == 'musician':
        return render_template('dashboard.html')


@app.route('/match-queue')
def match_queue():
    """Displays potential matches"""

    user_type = session.get('user_type')
    user_id = session.get('user_id')

    if user_type == None:
        return  redirect ('/login')
    if user_type == 'band':
        #musicians = []
        #for musician musicians 
            #if skill in user_id.band_skills
            #show musician profile #### So i need a crud display info function?
        return render_template('match-queue.html')
    if user_type == 'musician':
        return render_template('match-queue.html')


@app.route('/matched')
def matched():
    """Displays profiles the user has matched with"""
    user_type = session.get('user_type')

    if user_type == None:
        return  redirect ('/login')
    if user_type == 'band':
        return render_template('matched.html')
    if user_type == 'musician':
        return render_template('matched.html')


##Condense into 1 function most likely 
# @app.route('/users/<musician_id>') ###
# def musician_profile(musician_id):
#     """View a musician's profile"""

#     musician = crud.get_musician_by_id(musician_id)

#     return render_template('user_profile.html', musician=musician_id)

# @app.route('/users/<band_id>')  ###
# def band_profile(band_id):
#     """View a band's profile"""

#     band = crud.get_band_by_id(band_id)

#     return render_template('user_profile.html', band=band_id)

###Contact match###
#twilio api key




if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')


