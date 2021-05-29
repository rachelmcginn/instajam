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


@app.route('/login')
def login():
    """Log in"""
    return render_template('login.html')


@app.route('/sign-up')
def sign_up():
    """Displays sign up options."""
    return render_template('sign-up.html')


###################################################################
#Once logged in: retrieve display_name 
@app.route('/handle-login-band', methods = ['POST'])
def handle_login_band():
    """Handles log in"""

    email = request.form['email']
    password = request.form['password']
    
    user = crud.get_band_by_email(email)

    # #if user selects band 
    #     user = crud.get_band_by_email(email)
    #     #retrieve display_name
    # #if user selects musician 
    #     user = crud.get_musician_by_email(email)
    #     #retrieve display_name 

    if user == None:
        flash('Account does not exist. Please try again.')
        return redirect ('/')
    else:
        if (password == user.password):
            session['user_type'] = 'band' ############### Check what kind of user they are
            session['user_id'] = user.band_id #If band, swap in band_id. if musician, swap in musician_id
            
            flash(f'Logged in as {email}')
            return redirect ('/dashboard')  
        else:
            flash('Incorrect Password. Please try again.')
            return redirect ('/')  


@app.route('/handle-login-musician', methods = ['POST'])
def handle_login_musician():
    """Handles log in for musician"""

    email = request.form['email']
    password = request.form['password']
    
    user = crud.get_musician_by_email(email)
    
    # #if user selects musician 
    #     user = crud.get_musician_by_email(email)
    #     #retrieve display_name 

    if user == None:
        flash('Account does not exist. Please try again.')
        return redirect ('/')
    else:
        if (password == user.password):
            session['user_type'] = 'musician' ############### Check what kind of user they are
            session['user_id'] = user.musician_id #If band, swap in band_id. if musician, swap in musician_id
            
            flash(f'Logged in as {email}')
            return redirect ('/dashboard')  
        else:
            flash('Incorrect Password. Please try again.')
            return redirect ('/')  



@app.route('/set-session')
def set_session():

    session['user_id'] = 1
    session['user_type'] = 'band' ############ 
        #Instead of 'band': check what kind of user 
        #obtain id

    return redirect ('display-session.html')


@app.route('/display-session')
def display_session():

    print(session)

    return render_template('display-session.html')


# @app.route('/musician-login', methods = ['POST'])
# def musician_login():
#     """Logs in musician"""

#     email = request.form['email']
#     incoming_password = request.form['password']
#     user = crud.get_musician_by_email(email)
#     if user == None:
#         flash('Account does not exist. Please try again.')
#         return redirect ('/')
#     # else:
#     #     if (incoming_password == musician.password):
#     #         return redirect ('/dashboard.html')  
#     #     else:
#     #         flash('Incorrect Password. Please try again.')
#     #         return redirect ('/')  


@app.route('/dashboard')
def dashboard():
    """Displays dashboard to logged in user"""
    ##If signed in show dashboard, otherwise redirect to login page
    display_name = "(Insert Display Name Here)" ####################
    return render_template('dashboard.html',
                            display_name=display_name)


##Condense into 1 function most likely
# @app.route('/user-profile/<band_id>')
# def band_profile():
#     """Displays the profile of currently logged in band user"""
#     return render_template('user-profile.html')

# @app.route('/user-profile/<musician_id>')
# def musician_profile():
#     """Displays the profile of currently logged in musician user"""
#     return render_template('user-profile.html')


@app.route('/match-queue')
def jam_queue():
    """View potential matches"""
    return render_template('match-queue.html')


@app.route('/matches')
def matches():
    """Displays profiles the user has matched with"""
    return render_template('matches.html')


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




if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')


