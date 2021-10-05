'''
CLASSES FOR DATABASE BELOW
these tell SQLAlchemy how to take the data from Go.db and make it useable in Python
'''
from sqlalchemy.sql.schema import ForeignKey
from main import db

class users(db.Model):
    __tablename__ = 'user'
    userId = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    gamesWon = db.Column(db.Integer)
    gamesLost = db.Column(db.Integer)
    sessionId = db.Column(db.Integer)

class profile_pictures(db.Model):
    __tablename__ = 'profile_pictures'
    pictureId = db.Column(db.Integer, primary_key=True)
    pictureRef = db.Column(db.String)

class user_to_picture(db.Model):
    __tablename__ = 'user_to_picture'
    user_to_pictureId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.userId'))
    pictureRef = db.Column(db.String, db.ForeignKey('profile_pictures.pictureRef')) 

class game(db.Model): 
    __tablename__ = 'game'
    gameId = db.Column(db.Integer, primary_key=True)
    move1 = db.Column(db.String)
    move2 = db.Column(db.String)
    username1 = db.Column(db.String, db.ForeignKey('user.username'))
    username2 = db.Column(db.String, db.ForeignKey('user.username'))

# db.create_all(extend_existing=True)
# db.create_all()