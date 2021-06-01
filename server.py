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
    display_name = session.get('display_name')
    
    session['user_id'] = user_id
    session['user_type'] = user_type
    session['display_name'] = display_name

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
    
    skill = request.form['skill']
    genre = request.form['genre']
    
    user = crud.get_band_by_email(email)
    
    if user:
        flash("Band already exists, please log in.")
    else:
        band = crud.create_band(email, password, display_name, age, gender, influences, location, description)
        saved_skills = crud.add_a_band_skill(band, skill)
        saved_genres = crud.add_a_band_genre(band, genre)

        flash("Band profile successfully created!")
        return render_template("login.html")

### add skill/add genre not showing up in db #####
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

    skill = request.form['skill']
    genre = request.form['genre']

    user = crud.get_musician_by_email(email)

    if user:
        flash("Musician already exists, please log in.")
    else:
        musician = crud.create_musician(email, password, display_name, age, gender, influences, location, description)
        saved_skills = crud.add_a_musician_skill(musician, skill)
        saved_genres = crud.add_a_musician_genre(musician, genre)
        
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
            session['display_name'] = user.display_name 
            
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
            session['display_name'] = user.display_name 
            
            flash(f'Logged in as {email}')
            return redirect ('/dashboard')  
        else:
            flash('Incorrect Password. Please try again.')
            return redirect ('/')  


@app.route('/dashboard')
def dashboard():
    """Displays dashboard to logged in user"""

    user_type = session.get('user_type') 
    user_id = session.get('user_id')
    
    if user_type == None:
        return  redirect ('/login')

    if user_type == 'band':
        band = crud.get_band_by_id(user_id)

        display_name = band.display_name
        age = band.age
        gender = band.gender #may need to tweak this for bands (plural gender)
        influences = band.influences
        location = band.location
        description = band.description
        return render_template('dashboard.html',
                                display_name=display_name,
                                age=age,
                                gender=gender,
                                influences=influences,
                                location=location,
                                description=description) 

    if user_type == 'musician':
        musician = crud.get_musician_by_id(user_id)

        display_name = musician.display_name
        age = musician.age
        gender = musician.gender 
        influences = musician.influences
        location = musician.location
        description = musician.description

        return render_template('dashboard.html',
                                display_name=display_name,
                                age=age,
                                gender=gender,
                                influences=influences,
                                location=location,
                                description=description)


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
            #render musician profile 
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


