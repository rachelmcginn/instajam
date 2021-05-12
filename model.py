from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     """Data model for generic user."""

#     __tablename__ = "users"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     email = db.Column(db.Text, nullable=False, unique=True) 
#     password = db.Column(db.VARCHAR(20), nullable=False)
#     display_name = db.Column(db.VARCHAR(50), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     gender = db.Column(db.Text, nullable=False)
#     influences = db.Column(db.VARCHAR(250), nullable=False)
#     location = db.Column(db.VARCHAR(50), nullable=False)
#     description = db.Column(db.VARCHAR(250), nullable=False)

#     band = db.relationship('Band') ########## 
#     musician = db.relationship('Musician') #########

#     def __repr__(self):
#         return f'<User display_name={self.display_name} user_id={self.user_id} email={self.email}>'

class Band(db.Model):
    """Data model for a band user."""

    __tablename__ = "bands"

    band_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True) 
    password = db.Column(db.VARCHAR(20), nullable=False)
    display_name = db.Column(db.VARCHAR(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    influences = db.Column(db.VARCHAR(250), nullable=False)
    location = db.Column(db.VARCHAR(50), nullable=False)
    description = db.Column(db.VARCHAR(250), nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    #user = db.relationship('User') ########### 
    skills = db.relationship('Skill', secondary='band_skills')

    def __repr__(self):
        return f'<Band band_id={self.band_id} display_name={self.display_name}>'

class Musician(db.Model):
    """Data model for a musician user."""

    __tablename__ = "musicians"

    musician_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True) 
    password = db.Column(db.VARCHAR(20), nullable=False)
    display_name = db.Column(db.VARCHAR(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    influences = db.Column(db.VARCHAR(250), nullable=False)
    location = db.Column(db.VARCHAR(50), nullable=False)
    description = db.Column(db.VARCHAR(250), nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    
    #user = db.relationship('User') ########## 
    skills = db.relationship('Skill', secondary='musician_skills')

    def __repr__(self):
        return f'<Musician musician_id={self.musician_id} display_name={self.display_name}>'

class Skill(db.Model):
    """Data model for all selectable skills."""

    __tablename__ = "skills"

    skill_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    skill_name = db.Column(db.VARCHAR(50), nullable=False)

    bands = db.relationship('Band', secondary='band_skills')
    musicians = db.relationship('Musician', secondary='musician_skills')

    def __repr__(self):
        return f'<Skill skill_id={self.skill_id} skill_name={self.skill_name}>'

class Genre(db.Model):
    """Data model for all selectable genres."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    genre_name = db.Column(db.VARCHAR(20), nullable=False)

    bands = db.relationship('Band', secondary='band_genres')
    musicians = db.relationship('Musician', secondary='musician_genres')

    def __repr__(self):
        return f'<Genre genre_id={self.genre_id} genre_name={self.genre_name}>'

class BandGenre(db.Model):
    """Intermediate table connecting bands and genres"""

    __tablename__ = "band_genres"

    band_genres = db.Column(db.Text, nullable=False, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey('bands.band_id'), nullable=False)

    genres = db.relationship('Genre')
    bands = db.relationship('Band') 

    def __repr__(self):
        return f'<BandGenre genre_name={self.genre_name} genre_id={self.genre_id} display_name={self.display_name} band_id={self.band_id}>'

class MusicianGenre(db.Model):
    """Intermediate table connecting musicians and genres"""

    __tablename__ = "musician_genres"

    musician_genres = db.Column(db.Text, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    musician_id = db.Column(db.Integer, db.ForeignKey('musicians.musician_id'), nullable=False)

    genres = db.relationship('Genre') 
    musician = db.relationship('Musician')

    def __repr__(self):
        return f'<MusicianGenre genre_name={self.genre_name} genre_id={self.genre_id} display_name={self.display_name} musician_id={self.musician_id}>'

class BandSkill(db.Model):
    """Intermediate table connecting bands and skills."""

    __tablename__ = "band_skills"

    skill_id = db.Column(db.Integer, db.ForeignKey('skills.skill_id'), primary_key=True)
    band_id = db.Column(db.Integer, db.ForeignKey('bands.band_id'), primary_key=True)

    skills = db.relationship('Skill')
    bands = db.relationship('Band') 

    def __repr__(self):
        return f'<BandSkill skill_name={self.skill_name} skill_id={self.skill_id} diplay_name={self.display_name} band_id={self.band_id}>'

class MusicianSkill(db.Model):
    """Intermediate table connecting musicians and skills."""

    __tablename__ = "musician_skills"

    skill_id = db.Column(db.Integer, db.ForeignKey('skills.skill_id'), primary_key=True)
    musician_id = db.Column(db.Integer, db.ForeignKey('musicians.musician_id'), primary_key=True)

    skills = db.relationship('Skill')
    musicians = db.relationship('Musician') 

    def __repr__(self):
        return f'<MusicianSkill skill_name={self.skill_name} skill_id={self.skill_id} display_name={self.display_name} musician_id={self.musician_id}>'





def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///instajam'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    app.app_context().push()

if __name__ == '__main__':
    from server import app
    
    connect_to_db(app)
    print('Connected to db')