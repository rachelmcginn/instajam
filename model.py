from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Data model for generic user."""

    __tablename__ = "users"

    user_id = db.Column(db.Text, nullable=False, primary_key=True)
    email = db.Column(db.Text, nullable=False) 
    display_name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    influences = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        pass

class Band_users(db.Model):
    """Data model for a band user."""

    __tablename__ = "band_users"

    band_id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    email = db.Column(db.Text, nullable=False) 
    display_name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    influences = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    #relationship to users

    def __repr__(self):
        pass

class Musician_users(db.Model):
    """Data model for a musician user."""

    __tablename__ = "musician_users"

    musician_id = db.Column(db.Text, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    email = db.Column(db.Text, nullable=False) 
    display_name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    influences = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    #relationship to users and genres

    def __repr__(self):
        pass

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








if __name__ == '__main__':
    from server import app

    
    connect_to_db(app)
    print('Connected to db')