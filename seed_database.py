"""Script to seed database"""
import os 
import json

import crud
import model 
import server 

from crud import create_a_genre, create_a_skill, create_musician, create_band
from model import db, Skill, Genre, Band, Musician, BandSkill, MusicianSkill, BandGenre, MusicianGenre, connect_to_db

os.system('dropdb instajam')
os.system('createdb instajam')

model.connect_to_db(server.app)
model.db.create_all()

with open('./data/genres.json') as f:
    genre_data = json.loads(f.read())

    for genre in genre_data:
        create_a_genre(genre)


with open('./data/skills.json') as f:
    skill_data = json.loads(f.read())

    for skill in skill_data:
        create_a_skill(skill)


with open('./data/musicians.json') as f:
    musician_data = json.loads(f.read())

    for dict in musician_data:
        musician = create_musician(email=dict['email'],
                                    password=dict['password'],
                                    display_name=dict['display_name'],
                                    age=dict['age'],
                                    gender=dict['gender'],
                                    influences=dict['influences'],
                                    location=dict['location'],
                                    description=dict['description'],
                                    skills=dict['skills']) 

    db.session.add(musician)
    db.session.commit()

with open('./data/bands.json') as f:
    band_data = json.loads(f.read())

    for dict in band_data:
        band = create_band(email=dict['email'],
                            password=dict['password'],
                            display_name=dict['display_name'],
                            age=dict['age'],
                            gender=dict['gender'],
                            influences=dict['influences'],
                            location=dict['location'],
                            description=dict['description'])

    db.session.add(band)
    db.session.commit()