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
    email = db.Column(db.Text, nullable=False) 
    display_name = db.Column(varchar(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    influences = db.Column(varchar(250), nullable=False)
    location = db.Column(varchar(50), nullable=False)
    description = db.Column(varchar(250), nullable=False)

    #relationship to users

    def __repr__(self):
        pass

class BandGenres(db.Model):
    """Intermediate table connecting Band_users and Genres."""

    __tablename__ = "BandGenres"

    ##what is the primary key going to be 
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey('band_user.band_id'), nullable=False)

    def __repr__(self):
        pass

class Band_user_genres(db.Model):
    """Contains the selected genres of a given band user."""

    __tablename__ = "band_user_genres"

    ##what is the primary key going to be 
    ##do i need forgein key
    band_genre = db.Column(db.Text, nullable=False, primary_key=True)

    def __repr__(self):
        pass

class BandSkills(db.Model):
    """Intermediate table connecting band_users and all_skills."""

    __tablename__ = "BandSkills"

    ##what is the primary key going to be 
    band_skills = db.Column(db.Integer, nullable=False, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('all_skills.skill_id'), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey('band_users.band_id'), nullable=False)

    def __repr__(self):
        pass

class Band_user_skills(db.Model):
    """Contains the selected skills of a given band user."""

    __tablename__ = "band_user_skills"

    ##what is the primary key going to be 
    ##do i need forgein key
    skill_id = db.Column(db.Text, db.ForeignKey('BandSkills.bandskills_id'), nullable=False)

    def __repr__(self):
        pass

class Musician_users(db.Model):
    """Data model for a musician user."""

    __tablename__ = "musician_users"

    musician_id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    email = db.Column(db.Text, nullable=False) 
    display_name = db.Column(varchar(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    influences = db.Column(varchar(250), nullable=False)
    location = db.Column(varchar(50), nullable=False)
    description = db.Column(varchar(250), nullable=False)


    #relationship to users and genres

    def __repr__(self):
        pass










if __name__ == '__main__':
    from server import app

    
    connect_to_db(app)
    print('Connected to db')