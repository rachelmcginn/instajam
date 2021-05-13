from typing import NoReturn
from model import db, Skill, Genre, Band, Musician, BandSkill, MusicianSkill, BandGenre, MusicianGenre, connect_to_db
import os

def create_musician(email, password, display_name, age, gender, influences, location, description):
    """Create and return a new musician"""

    musician = Musician(email=email,
                        password=password, 
                        display_name=display_name,
                        age=age,
                        gender=gender,
                        influences=influences,
                        location=location,
                        description=description)

    db.session.add(musician)
    db.session.commit()

    return musician

def create_band(email, password, display_name, age, gender, influences, location, description):
    """Create and return a new band"""

    band = Band(email=email,
                password=password, 
                display_name=display_name,
                age=age,
                gender=gender,
                influences=influences,
                location=location,
                description=description)

    db.session.add(band)
    db.session.commit()

    return band

def create_skill(skill_name):
    """Create new skill."""

    skill = Skill(skill_name=skill_name)

    db.session.add(Skill(skill_name=skill))
    db.session.commit()

    return skill


def create_a_test_musician():
    """Creates a test musician"""
    email = 'ted@test.com'
    password = '1234'
    display_name = 'ted shreds'
    age = 21
    gender = 'm'
    influences = 'the beatles'
    location = 'nyc'
    description = "Hey I'm Ted & I play the guitar."

    test_musician = Musician(email=email, password=password, display_name=display_name,
        age=age, gender=gender, influences=influences, location=location,
        description=description)

    db.session.add(test_musician)
    db.session.commit()
    return test_musician


def create_a_test_band():
    """Creates a test band"""
    email = 'bill@test.com'
    password = '5678'
    display_name = 'bills band'
    age = 22
    gender = 'm'
    influences = 'the rolling stones'
    location = 'boston'
    description = "Hi I'm Bill. Looking for a bassist."

    test_band = Band(email=email, password=password, display_name=display_name,
        age=age, gender=gender, influences=influences, location=location,
        description=description)

    db.session.add(test_band)
    db.session.commit()
    return test_band

def seed_test_data():
    """Seeds test data to the db."""
    os.system('dropdb instajam')
    os.system('createdb instajam')
    db.create_all()

    #adds sample skills to db 
    # guitar = Skill(skill_name='guitar')
    # db.session.add(guitar)
    # bass = Skill(skill_name='bass')
    # db.session.add(bass)
    # banjo = Skill(skill_name='banjo')
    # db.session.add(banjo)
    # piano = Skill(skill_name='piano')
    # db.session.add(piano)

    #adds sample genres to db 
    # rock = Genre(genre_name='rock')
    # db.session.add(rock)
    # experimental = Genre(genre_name='experimental')
    # db.session.add(experimental)
    # folk = Genre(genre_name='folk')
    # db.session.add(folk)
    # jazz = Genre(genre_name='jazz')
    # db.session.add(jazz)
    
    #creates ted as a musician user & bill as a band user 
    ted_musician = create_a_test_musician()
    bills_band = create_a_test_band()

    # ted_musician.skills.append('bass')
    # ted_musician.skills.append('banjo')
    # ted_musician.genres.append('rock')
    # ted_musician.genres.append('folk')
    # db.session.add(ted_musician)

    # db.session.commit()
    
    # bills_band.skills.append('bass')
    # bills_band.skills.append('piano')
    # bills_band.genres.append('rock')
    # bills_band.genres.append('jazz')
    # db.session.add(bills_band)

    db.session.commit()
    
def create_a_skill(skill):
    """Add a new skill to the db"""
    skill = Skill(skill_name=skill)
    db.session.add(skill)
    db.session.commit()

    return skill

def create_a_genre(genre):
    """Add a genre to the db"""
    genre = Genre(genre_name=genre)
    db.session.add(genre)
    db.session.commit()
    
    return genre

def add_a_musician_skill(musician, skill): ###Currently working on 
    """Add a skill to a musician's profile"""
    skill = Skill(skill_name=skill)
    musician = Musician(musician_id=musician)

    return skill

def add_a_musician_genre(musician, genre):
    """Add a genre to a musician's profile"""
    return genre

def add_a_band_skill(band, skill):
    """Add a skill to a band's profile"""
    return skill

def add_a_band_genre(band, skill):
    """Add a skill to a band's profile"""
    return skill

def match_user(user_match):
    """Match a user"""

    user_match = ""

    return user_match

def display_matches(matches):
    """Display all matches"""
    matches = ""
    return matches    

if __name__ == '__main__':
    from server import app

    
    connect_to_db(app)
    print('Connected to db!')