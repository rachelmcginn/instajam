from model import Band, Musician
from crud import create_band, create_musician, find_matches
from flask import (Flask, render_template, request, flash, session, redirect)

import crud
import os
from model import connect_to_db
from jinja2 import StrictUndefined
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID'] 
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_PHONE_NUMBER'] 

client = Client(account_sid, auth_token)

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

    user_type = session.get('user_type')
    user_id = session.get('user_id')

    if user_type != None:
        user = crud.get_band_by_id(user_id)

        display_name = user.display_name
    else:
        display_name = "Guest"
        
    return render_template('home.html',
                            user_type=user_type,
                            user_id=user_id,
                            display_name=display_name)


@app.route('/create-band')
def create_band(): 
    """Displays form to create a new band user"""
    
    user_type = session.get('user_type')
    user_id = session.get('user_id')
    
    return render_template('create-band.html',
                            user_type=user_type,
                            user_id=user_id)


@app.route('/handle-create-band', methods=['POST'])
def handle_create_band(): 
    """Handles new band user"""

    user_type = session.get('user_type')
    user_id = session.get('user_id')
    
    email = request.form['email']
    password = request.form['password']
    display_name = request.form['display_name']
    age = request.form['age']
    gender = request.form['gender']
    influences = request.form['influences']
    location = request.form['location']
    description = request.form['description']
    
    skill_list = request.form.getlist('skills')
    genre_list = request.form.getlist('genres')
    
    user = crud.get_band_by_email(email)
    
    if user:
        flash("Band already exists, please log in.")
        return render_template("login.html",
                            user_type=user_type,
                            user_id=user_id) 
    else: 
        band = crud.create_band(email, password, display_name, age, gender, influences, location, description, skill_list, genre_list)

        flash("Band profile successfully created!")
        return render_template("login.html",
                            user_type=user_type,
                            user_id=user_id)
    

@app.route('/create-musician')
def create_musician(): 
    """Displays form to create a new musician user"""
    
    user_type = session.get('user_type')
    user_id = session.get('user_id')
    
    return render_template('create-musician.html',
                            user_type=user_type,
                            user_id=user_id)


@app.route('/handle-create-musician', methods=['POST'])
def handle_create_musician(): 
    """Handles new musician user"""

    user_type = session.get('user_type')
    user_id = session.get('user_id')
    
    email = request.form['email']
    password = request.form['password']
    display_name = request.form['display_name']
    age = request.form['age']
    gender = request.form['gender']
    influences = request.form['influences']
    location = request.form['location']
    description = request.form['description']

    skill_list = request.form.getlist('skills')
    genre_list = request.form.getlist('genres')

    user = crud.get_musician_by_email(email)

    if user:
        flash("Musician already exists, please log in.")
        return render_template("login.html",
                                user_type=user_type,
                                user_id=user_id)
    else:
        musician = crud.create_musician(email, password, display_name, age, gender, influences, location, description, skill_list, genre_list)
    
        flash("Musician profile successfully created!")
        return render_template("login.html",
                                user_type=user_type,
                                user_id=user_id)


# @app.route('/sign-up')
# def sign_up():
#     """Displays sign up options."""
#     return render_template('sign-up.html')


@app.route('/login')
def login():
    """Log in user"""

    user_type = session.get('user_type')
    user_id = session.get('user_id')

    return render_template('login.html',
                            user_type=user_type,
                            user_id=user_id)

@app.route ('/logout')
def logout():
    """Log out user"""

    session.clear()
    flash("See you next time!")
    return redirect('/')


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
        gender = band.gender 
        influences = band.influences
        location = band.location
        description = band.description
        seeking = band.skills
        genres = band.genres

        return render_template('dashboard.html',
                                user_type=user_type,
                                display_name=display_name,
                                age=age,
                                gender=gender,
                                influences=influences,
                                location=location,
                                description=description,
                                seeking=seeking,
                                genres=genres) 

    if user_type == 'musician':
        musician = crud.get_musician_by_id(user_id)

        display_name = musician.display_name
        age = musician.age
        gender = musician.gender 
        influences = musician.influences
        location = musician.location
        description = musician.description
        skills = musician.skills
        genres = musician.genres

        return render_template('dashboard.html',
                                user_type=user_type,
                                display_name=display_name,
                                age=age,
                                gender=gender,
                                influences=influences,
                                location=location,
                                description=description,
                                skills=skills,
                                genres=genres)


@app.route('/matches')
def match_queue():
    """Displays potential matches"""
    
    user_type = session.get('user_type')
    user_id = session.get('user_id')

    if user_type == None:
        return  redirect ('/login')
    elif user_type == 'band':
        current_band = Band.query.get(user_id)
        found_matches = crud.find_matches(current_band)
        if found_matches == []:
            flash("No matches found. Check back again soon!")
            return render_template("matches.html")  
        return render_template('matches.html',
                                found_matches=found_matches,
                                user_type=user_type)
    elif user_type == 'musician':
        current_musician = Musician.query.get(user_id)
        found_matches = crud.find_matches(current_musician)
        if found_matches == []:
            flash("No matches found. Check back again soon!")
            return render_template("matches.html")  
        return render_template('matches.html',
                                found_matches=found_matches,
                                user_type=user_type)


@app.route('/contact-match', methods=['POST'])
def send_twilio_sms():
    
    match_name = request.form.get("display_name")
    match_email = request.form.get("email")
    phone_input = request.form.get("phone_input")

    user_type = session.get('user_type')
    user_id = session.get('user_id')

    if user_type == None:
        return  redirect ('/login')
    elif user_type == 'band':
        current_band = Band.query.get(user_id)
        found_matches = crud.find_matches(current_band)
    elif user_type == 'musician':
        current_musician = Musician.query.get(user_id) 
        found_matches = crud.find_matches(current_musician)
        
    msg = f"\nHello from Instajam!\nYou can reach {match_name} at {match_email}.\nHappy Jamming!",
    
    message = client.messages \
                    .create(
                        body=msg,
                        from_=twilio_number,
                        to=phone_input
                    )

    return render_template('matches.html',
                            match_name=match_name,
                            match_email=match_email,
                            phone_input=phone_input,
                            message=message,
                            found_matches=found_matches,
                            user_type=user_type,
                            user_id=user_id)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')


