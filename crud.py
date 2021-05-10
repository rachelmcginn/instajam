from model import db, Skill, Genre, User, Band, Musician, BandSkills, MusicianSkills, BandGenres, MusicianGenres, connect_to_db
import os

###Notes: Skills and Genres will be hardcoded

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

def create_band(band_id):
    """Create and return a new band"""
    
    band = Band(user_id=user_id)

    db.session.add(band)
    db.session.commit()

    return band



# def create_a_test_user():
#     email = 'test2@test.com'
#     password = '1234'
#     display_name = 'bob2'
#     age = 21
#     gender = 'm'
#     influences = 'the beatles'
#     location = 'nyc'
#     description = 'this is my description'

#     test_user_2 = User(email=email, password=password, display_name=display_name,
#         age=age, gender=gender, influences=influences, location=location,
#         description=description)

#     db.session.add(test_user_2)
#     db.session.commit()
#     return test_user_2

# def seed_test_data():
#     os.system('dropdb instajam')
#     os.system('createdb instajam')
#     db.create_all()

#     skill1 = 'guitar'
#     skill2 = 'bass'

#     db.session.add(Skill(skill_name=skill1))
#     db.session.add(Skill(skill_name=skill2))
    
    
#     bob = create_a_test_user()

#     db.session.add(Musician_users(user=bob))
#     db.session.commit()
    
    

if __name__ == '__main__':
    from server import app

    
    connect_to_db(app)
    print('Connected to db')