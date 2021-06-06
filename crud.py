from typing import NoReturn
from model import db, Skill, Genre, Band, Musician, BandSkill, MusicianSkill, BandGenre, MusicianGenre, connect_to_db
import os

def create_musician(email, password, display_name, age, gender, influences, location, description): #pass in skills 
    """Create and return a new musician"""

    musician = Musician(email=email,
                        password=password, 
                        display_name=display_name,
                        age=age,
                        gender=gender,
                        influences=influences,
                        location=location,
                        description=description)
    #create musician 
    #check through list of skill objects
    #add the chosen skills to musician 

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


def add_a_band_skill(band, skill_list): #tweak name
    """Add a skill to a band's profile"""
    #Need ability to add multiple skills
    print(band)
    print(skill_list)
    band_skills = []

    found_skills = Skill.query.filter(Skill.skill_name.in_(skill_list)).all()
    print(found_skills)

                    
    for skill in found_skills:
        band_skill = BandSkill(skill_id=skill.skill_id,
                            band_id=band.band_id)
        band_skills.append(band_skill)
        print(band_skills)

        db.session.add(band_skill)

    db.session.commit()

    return band_skills

#########################################################

def add_a_musician_skill(musician, skill): 
    """Add a skill to a musician's profile"""
    #Need ability to add multiple skills 

    found_skill = Skill.query.filter(Skill.skill_name==skill).first()
    musician_skills = MusicianSkill(skill_id=found_skill.skill_id,
                                    musician_id=musician.musician_id)

    db.session.add(musician_skills)
    db.session.commit()

    return musician_skills


def add_a_band_genre(band, genre):
    """Add a genre to a band's profile"""
    #Need ability to add multiple genres

    found_genre = Genre.query.filter(Genre.genre_name==genre).first()
    band_genres = BandGenre(genre_id=found_genre.genre_id,
                            band_id=band.band_id)

    db.session.add(band_genres)
    db.session.commit()

    return band_genres

def add_a_musician_genre(musician, genre):
    """Add a genre to a musician's profile"""
    #Need ability to add multiple genres

    found_genre = Genre.query.filter(Genre.genre_name==genre).first()
    musician_genres = MusicianGenre(genre_id=found_genre.genre_id,
                                    musician_id=musician.musician_id)

    db.session.add(musician_genres)
    db.session.commit()

    return musician_genres


def get_musician_by_id(musician_id):
    """"Returns musician's ID."""

    return Musician.query.get(musician_id)


def get_band_by_id(band_id):
    """"Returns a band's ID."""

    return Band.query.get(band_id)


def get_band_by_email(email):
    """Return user if band exists."""

    return Band.query.filter(Band.email == email).first()

def get_musician_by_email(email):
    """Return user if musician exists."""

    return Musician.query.filter(Musician.email == email).first()


def find_matching_bands(musician):
    """Finds matching bands"""
    matches = set()
    bands = Band.query.all()
    musician_skills = musician.skills
    musician_genres = musician.genres

    for band in bands:
        matching_skill = False 
        matching_genre = False 

        for skill in band.skills:
            if skill in musician_skills:
                matching_skill = True
                break 

        for genre in band.genres:
            if genre in musician_genres:
                matching_genre = True

        if matching_skill and matching_genre == True:        
            matches.add(band)

    return matches
        

def find_matching_musicians(band):
    """Finds matching musicians"""

def find_matches(user):
    """Match with another user"""
    
    if isinstance(user, Band):
        return find_matching_musicians(user)
    else:
        return find_matching_bands(user)

    return matched_user

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