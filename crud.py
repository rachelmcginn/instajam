from typing import NoReturn
from model import db, Skill, Genre, Band, Musician, BandSkill, MusicianSkill, BandGenre, MusicianGenre, connect_to_db
import os

################################ rachel start 
def create_musician(email, password, display_name, age, gender, influences, location, description, skill_list, genre_list):  
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

    found_skills = Skill.query.filter(Skill.skill_name.in_(skill_list)).all()
    found_genres = Genre.query.filter(Genre.genre_name.in_(genre_list)).all()
    
    musician_skills = []
    musician_genres = []
    
    for skill in found_skills:
        musician_skill = MusicianSkill(skill_id=skill.skill_id,
                                        musician_id=musician.musician_id)
        musician_skills.append(musician_skill)
        db.session.add(musician_skill)
        
    db.session.commit()

    for genre in found_genres:
        musician_genre = MusicianGenre(genre_id=genre.genre_id,
                                        musician_id=musician.musician_id)
        musician_genres.append(musician_genre)
        db.session.add(musician_genre)
    
    db.session.commit()

    return musician


def create_band(email, password, display_name, age, gender, influences, location, description, skill_list, genre_list):
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

    found_skills = Skill.query.filter(Skill.skill_name.in_(skill_list)).all()
    found_genres = Genre.query.filter(Genre.genre_name.in_(genre_list)).all()

    band_skills = []
    band_genres = []
    
    for skill in found_skills:
        band_skill = BandSkill(skill_id=skill.skill_id,
                                band_id=band.band_id)
        band_skills.append(band_skill)
        db.session.add(band_skill)
    
    db.session.commit()

    for genre in found_genres:
        band_genre = BandGenre(genre_id=genre.genre_id,
                                        band_id=band.band_id)
        band_genres.append(band_genre)
        db.session.add(band_genre)
    
    db.session.commit()

    return band

###################################################### end 

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


def add_band_skills(band, skill_list):
    """Add a skill to a band's profile"""
    
    band_skills = []

    found_skills = Skill.query.filter(Skill.skill_name.in_(skill_list)).all()

                    
    for skill in found_skills:
        band_skill = BandSkill(skill_id=skill.skill_id,
                            band_id=band.band_id)
        band_skills.append(band_skill)


        db.session.add(band_skill)

    db.session.commit()

    return band_skills


def add_musician_skills(musician, skill_list): 
    """Add a skill to a musician's profile"""

    musician_skills = []

    found_skills = Skill.query.filter(Skill.skill_name.in_(skill_list)).all()

    for skill in found_skills:
        musician_skill = MusicianSkill(skill_id=skill.skill_id,
                            musician_id=musician.musician_id)
        musician_skills.append(musician_skill)


        db.session.add(musician_skill)

    db.session.commit()

    return musician_skills


def add_band_genres(band, genre_list):
    """Add genres to a band's profile"""

    band_genres = []

    found_genres = Genre.query.filter(Genre.genre_name.in_(genre_list)).all()
                    
    for genre in found_genres:
        band_genre = BandGenre(genre_id=genre.genre_id,
                            band_id=band.band_id)
        band_genres.append(band_genre)


        db.session.add(band_genre)

    db.session.commit()

    return band_genres

def add_musician_genres(musician, genre_list):
    """Add genres to a musician's profile"""

    musician_genres = []

    found_genres = Genre.query.filter(Genre.genre_name.in_(genre_list)).all()
                    
    for genre in found_genres:
        musician_genre = MusicianGenre(genre_id=genre.genre_id,
                            musician_id=musician.musician_id)
        musician_genres.append(musician_genre)


        db.session.add(musician_genre)

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
    
    matches = set()
    musicians = Musician.query.all()
    band_skills = band.skills
    band_genres = band.genres

    for musician in musicians:
        matching_skill = False 
        matching_genre = False 

        for skill in musician.skills:
            if skill in band_skills:
                matching_skill = True
                break 

        for genre in musician.genres:
            if genre in band_genres:
                matching_genre = True

        if matching_skill and matching_genre == True:        
            matches.add(musician)

    return matches


def find_matches(user):
    """Match with another user"""
    
    if isinstance(user, Band):
        return find_matching_musicians(user)
    else:
        return find_matching_bands(user)


# def show_matches(matches):
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