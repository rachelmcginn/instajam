"""Script to seed database"""
from crud import create_a_genre, create_a_skill
import os 
import json

import crud
import model 
import server 

os.system('dropdb instajam')
os.system('createdb instajam')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/genres.json') as f:
    genre_data = json.loads(f.read())

    for genre in genre_data:
        create_a_genre(genre)


with open('data/skills.json') as f:
    skill_data = json.loads(f.read())

    for skill in skill_data:
        create_a_skill(skill)

