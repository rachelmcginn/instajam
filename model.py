from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class All_skills(db.Model):
    """Data model for all selectable skills."""

    __tablename__ = "all_skills"

    skill_id = db.Column(db.Integer, nullable=False, primary_key=True)
    skill_name = db.Column(db.varchar(50), nullable=False)

    def __repr__(self):
        pass

class Genres(db.Model):
    """Data model for all selectable genres."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, nullable=False, primary_key=True)
    genre_name = db.Column(db.varchar(20), nullable=False)

    def __repr__(self):
        pass

###### User tables ######

class User(db.Model):
    """Data model for generic user."""

    __tablename__ = "users"

    user_id = db.Column(db.Text, nullable=False, primary_key=True)
    email = db.Column(db.Text, nullable=False) 
    display_name = db.Column(db.varchar(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    influences = db.Column(db.varchar(250), nullable=False)
    location = db.Column(db.varchar(50), nullable=False)
    description = db.Column(db.varchar(250), nullable=False)

    def __repr__(self):
        pass

class Band_users(db.Model):
    """Data model for a band user."""

    __tablename__ = "band_users"

    band_id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    #relationship to users

    def __repr__(self):
        pass

class Musician_users(db.Model):
    """Data model for a musician user."""

    __tablename__ = "musician_users"

    musician_id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    #relationship to users

    def __repr__(self):
        pass

class BandGenres(db.Model):
    """Intermediate table connecting band_users and band_user_genres"""

    __tablename__ = "BandGenres"

    band_genres = db.Column(db.Text, nullable=False, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey('band_users.band_id'), nullable=False)

    #relationships to genres and band_users

    def __repr__(self):
        pass

class MusicianGenres(db.Model):
    """Intermediate table connecting musician_users and musician_user_genres"""

    __tablename__ = "MusicianGenres"

    musician_genres = db.Column(db.Text, nullable=False, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    musician_id = db.Column(db.Integer, db.ForeignKey('musician_users.musician_id'), nullable=False)

    #relationships to genres and musician_users

    def __repr__(self):
        pass

class Band_user_genres(db.Model):
    """Contains the selected genres of a given band user."""

    __tablename__ = "band_user_genres"

    band_user_genres = db.Column(db.Text, nullable=False, primary_key=True)
    band_genres = db.Column(db.Text, db.ForeignKey('BandGenres.band_genres'), nullable=False)

    #relationship to BandGenre

    def __repr__(self):
        pass

class Musician_user_genres(db.Model):
    """Contains the selected genres of a given musician user."""

    __tablename__ = "musician_user_genres"

    musician_user_genres = db.Column(db.Text, nullable=False, primary_key=True)
    musician_genres = db.Column(db.Text, db.ForeignKey('MusicianGenres.musician_genres'), nullable=False)

    #relationship to MusicianGenre

    def __repr__(self):
        pass

class BandSkills(db.Model):
    """Intermediate table connecting band_users and band_user_skills."""

    __tablename__ = "BandSkills"

    band_skills = db.Column(db.Integer, nullable=False, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('all_skills.skill_id'), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey('band_users.band_id'), nullable=False)

    #relationships to all_skills and band_users

    def __repr__(self):
        pass

class MusicianSkills(db.Model):
    """Intermediate table connecting musician_users and musician_user_skills."""

    __tablename__ = "MusicianSkills"

    musician_skills = db.Column(db.Integer, nullable=False, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('all_skills.skill_id'), nullable=False)
    musician_id = db.Column(db.Integer, db.ForeignKey('musician_users.musician_id'), nullable=False)

    #relationships to all_skills and musician_users

    def __repr__(self):
        pass

class Band_user_skills(db.Model):
    """Contains the selected skills of a given band user."""

    __tablename__ = "band_user_skills"

    band_user_skills = db.Column(db.Text, nullable=False, primary_key=True)
    band_skills = db.Column(db.Text, db.ForeignKey('BandSkills.band_skills'), nullable=False)

    def __repr__(self):
        pass

class Musician_user_skills(db.Model):
    """Contains the selected skills of a given musician user."""

    __tablename__ = "musician_user_skills"

    musician_user_skills = db.Column(db.Text, nullable=False, primary_key=True)
    musician_skills = db.Column(db.Text, db.ForeignKey('BandSkills.musician_skills'), nullable=False)

    def __repr__(self):
        pass










if __name__ == '__main__':
    from server import app

    
    connect_to_db(app)
    print('Connected to db')