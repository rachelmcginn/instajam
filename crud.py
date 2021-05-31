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
    skill = Skill(skill_id=skill)
    musician = Musician(musician_id=musician)

    db.session.commit()

    return skill


def add_a_musician_genre(musician, genre):
    """Add a genre to a musician's profile"""
    genre = Genre(genre_name=genre)
    musician = Musician(musician_id=musician)

    db.session.commit()

    return genre


def add_a_band_skill(band, skill):
    """Add a skill to a band's profile"""
    print("I'm here!")
    print(band)
    print(skill)
    found_skill = Skill.query.filter(Skill.skill_name==skill).first()
    #db.session.query(Skill).filter(Skill.skill_name==skill)
    print(found_skill)
    
    #Musician.query.filter(Musician.email == email).first()
    band_skills = BandSkill(skill_id=found_skill.skill_id,
                            band_id=band.band_id)
    print(band_skills)

    db.session.add(band_skills)
    db.session.commit()

    return band_skills


def add_a_band_genre(band, genre):
    """Add a genre to a band's profile"""
    genre = Genre(genre_name=genre)
    band = Band(band_id=band)

    db.session.commit()

    return genre


def get_musician_by_id(musician_id):
    """"Returns musician by ID."""

    return Musician.query.get(musician_id)


def get_band_by_id(band_id):
    """"Returns band by ID."""

    return Band.query.get(band_id)


def get_musician_by_email(email):
    """Return user if musician exists."""

    return Musician.query.filter(Musician.email == email).first()


def get_band_by_email(email):
    """Return user if band exists."""

    return Band.query.filter(Band.email == email).first()


# def match_user(matched_user):
#     """Match with another user"""


#     return matched_user

# def see_matches(matches):
#     """See all matches"""
#     
#     return matches    

#View profile

#See potential matches

#Match with user

#See all matches




if __name__ == '__main__':
    from server import app

    
    connect_to_db(app)
    print('Connected to db!')