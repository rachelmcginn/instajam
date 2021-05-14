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


def add_a_musician_skill(musician, skill): 
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