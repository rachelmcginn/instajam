from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#####Questions:
#id's: auto increment? 
#"unique = True" for emails, etc?
#for intermediate tables: 
    # what kind of primary key makes sense
    # how are genres being stored


class All_skills(db.Model):
    """Data model for all selectable skills."""

    __tablename__ = "all_skills"

    skill_id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    skill_name = db.Column(db.varchar(50), nullable=False)

    def __repr__(self):
        return f'<All_skills skill_id={self.skill_id} skill_name={self.skill_name}>'

class Genres(db.Model):
    """Data model for all selectable genres."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    genre_name = db.Column(db.varchar(20), nullable=False)

    def __repr__(self):
        return f'<Genres genre_id={self.genre_id} genre_name={self.genre_name}>'


class User(db.Model):
    """Data model for generic user."""

    __tablename__ = "users"

    user_id = db.Column(db.Text, autoincrement=True, nullable=False, primary_key=True)
    email = db.Column(db.Text, nullable=False) 
    password = db.Column(db.varchar(20), nullable=False)
    display_name = db.Column(db.varchar(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    influences = db.Column(db.varchar(250), nullable=False)
    location = db.Column(db.varchar(50), nullable=False)
    description = db.Column(db.varchar(250), nullable=False)

    def __repr__(self):
        return f'<Genres user_id={self.user_id} email={self.email}>'

class Band_users(db.Model):
    """Data model for a band user."""

    __tablename__ = "band_users"

    band_id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    user = db.relationship('User')

    def __repr__(self):
        return f'<Band_users band_id={self.band_id} user_id={self.user_name}>'

class Musician_users(db.Model):
    """Data model for a musician user."""

    __tablename__ = "musician_users"

    musician_id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    user = db.relationship('User')

    def __repr__(self):
        return f'<Musician_users musician_id={self.musician_id} user_id={self.user_id}>'

class BandGenres(db.Model):
    """Intermediate table connecting band_users and band_user_genres"""

    __tablename__ = "BandGenres"

    band_genres = db.Column(db.Text, nullable=False, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey('band_users.band_id'), nullable=False)

    genres = db.relationship('Genres')
    band_users = db.relationship('Band_users')

    def __repr__(self):
        return f'<BandGenres genre_id={self.genre_id} band_id={self.band_id}>'

class MusicianGenres(db.Model):
    """Intermediate table connecting musician_users and musician_user_genres"""

    __tablename__ = "MusicianGenres"

    musician_genres = db.Column(db.Text, nullable=False, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    musician_id = db.Column(db.Integer, db.ForeignKey('musician_users.musician_id'), nullable=False)

    genres = db.relationship('Genres')
    musician_users = db.relationship('Musician_users')

    def __repr__(self):
        return f'<Genres genre_id={self.genre_id} musician_id={self.musician_id}>'

class Band_user_genres(db.Model):
    """Contains the selected genres of a given band user."""

    __tablename__ = "band_user_genres"

    band_user_genres = db.Column(db.Text, nullable=False, primary_key=True)
    band_genres = db.Column(db.Text, db.ForeignKey('BandGenres.band_genres'), nullable=False)

    BandGenre = db.relationship('BandGenre')

    def __repr__(self):
        return f'<Band_user_genres band_genres={self.band_genres}>'

class Musician_user_genres(db.Model):
    """Contains the selected genres of a given musician user."""

    __tablename__ = "musician_user_genres"

    musician_user_genres = db.Column(db.Text, nullable=False, primary_key=True)
    musician_genres = db.Column(db.Text, db.ForeignKey('MusicianGenres.musician_genres'), nullable=False)

    musicianGenre = db.relationship('MusicianGenre')

    def __repr__(self):
        return f'<Musician_user_genres musician_genres={self.musician_genres}>'

class BandSkills(db.Model):
    """Intermediate table connecting band_users and band_user_skills."""

    __tablename__ = "BandSkills"

    band_skills = db.Column(db.Integer, nullable=False, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('all_skills.skill_id'), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey('band_users.band_id'), nullable=False)

    all_skills = db.relationship('All_skills')
    band_users = db.relationship('Band_users')

    def __repr__(self):
        return f'<BandSkills skill_id={self.skill_id} band_id={self.band_id}>'

class MusicianSkills(db.Model):
    """Intermediate table connecting musician_users and musician_user_skills."""

    __tablename__ = "MusicianSkills"

    musician_skills = db.Column(db.Integer, nullable=False, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('all_skills.skill_id'), nullable=False)
    musician_id = db.Column(db.Integer, db.ForeignKey('musician_users.musician_id'), nullable=False)

    all_skills = db.relationship('All_skills')
    musician_users = db.relationship('Musician_users')

    def __repr__(self):
        return f'<MusicianSkills skill_id={self.skill_id} musician_id={self.band_id}>'

class Band_user_skills(db.Model):
    """Contains the selected skills of a given band user."""

    __tablename__ = "band_user_skills"

    band_user_skills = db.Column(db.Text, nullable=False, primary_key=True)
    band_skills = db.Column(db.Text, db.ForeignKey('BandSkills.band_skills'), nullable=False)

    bandSkills = db.relationship('BandSkills')
    
    def __repr__(self):
        return f'<Band_user_skills band_skills={self.band_skills}>'

class Musician_user_skills(db.Model):
    """Contains the selected skills of a given musician user."""

    __tablename__ = "musician_user_skills"

    musician_user_skills = db.Column(db.Text, nullable=False, primary_key=True)
    musician_skills = db.Column(db.Text, db.ForeignKey('BandSkills.musician_skills'), nullable=False)

    musicianSkills = db.relationship('MusicianSkills')

    def __repr__(self):
        return f'<Musician_user_skills musician_skills={self.musician_skills}>'










def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Instajam'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == '__main__':
    from server import app

    
    connect_to_db(app)
    print('Connected to db')