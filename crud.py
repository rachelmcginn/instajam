from typing import NoReturn
from model import db, Skill, Genre, User, Band, Musician, BandSkill, MusicianSkill, BandGenre, MusicianGenre, connect_to_db
import os

def create_user(email, password, display_name, age, gender, influences, location, description):
    """Create and return a new user"""

    user = User(email=email,
                password=password, 
                display_name=display_name,
                age=age,
                gender=gender,
                influences=influences,
                location=location,
                description=description)
    
    db.session.add(user)
    db.session.commit()

    return user

def create_musician(user_id):
    """Create and return a new musician"""

    musician = Musician(user_id=user_id)

    db.session.add(musician)
    db.session.commit()

    return musician

def create_band(user_id):
    """Create and return a new band"""

    band = Band(user_id=user_id)

    db.session.add(band)
    db.session.commit()

    return band

def create_skill(skill_name):
    """Create new skill."""

    skill = Skill(skill_name=skill_name)

    db.session.add(Skill(skill_name=skill))
    db.session.commit()

    return skill

def add_a_skill(skill):
    """Add a new skill to a user profile"""
    pass


    return skill

def add_a_genre(genre):
    """Add a genre to a user profile"""
    pass
    
    return genre

def match_user(user_match):
    """Match a user"""

    user_match = ""
    pass

    return user_match

def display_matches(matches):
    """Display all matches"""
    matches = ""
    pass
    return matches

def create_a_test_user():
    email = 'ted@test.com'
    password = '1234'
    display_name = 'ted'
    age = 21
    gender = 'm'
    influences = 'the beatles'
    location = 'nyc'
    description = 'this is my description'

    test_user = User(email=email, password=password, display_name=display_name,
        age=age, gender=gender, influences=influences, location=location,
        description=description)

    db.session.add(test_user)
    db.session.commit()
    return test_user


def create_a_test_user_2():
    email = 'bill@test.com'
    password = '5678'
    display_name = 'bill'
    age = 22
    gender = 'm'
    influences = 'the rolling stones'
    location = 'boston'
    description = 'my description goes here'

    test_user_2 = User(email=email, password=password, display_name=display_name,
        age=age, gender=gender, influences=influences, location=location,
        description=description)

    db.session.add(test_user_2)
    db.session.commit()
    return test_user_2

def seed_test_data():
    os.system('dropdb instajam')
    os.system('createdb instajam')
    db.create_all()

    guitar = Skill(skill_name='guitar')
    db.session.add(guitar)

    bass = Skill(skill_name='bass')
    db.session.add(bass)

    
    
    ted = create_a_test_user()
    bill = create_a_test_user_2()

    ted_musician = Musician(user=ted)
    ted_musician.skills.append(bass)
    db.session.add(ted_musician)

    
    bills_band = Band(user=bill)
    bills_band.skills.append(bass)

    db.session.add(bills_band)

    

    db.session.commit()
    
    

if __name__ == '__main__':
    from server import app

    
    connect_to_db(app)
    print('Connected to db!')