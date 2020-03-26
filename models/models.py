from PORTFOLIO.database import db
from sqlalchemy.orm import relationship

class Login(db.Model):
    __tablename__ = 'login'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    users = db.relationship("User", uselist=False, backref="login")
    roomAl1 = db.relationship("RoomAl1", uselist=False, backref="login")


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(255), nullable=False)
    lname = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)
    roomAl1 = db.relationship("RoomAl1", uselist=False, backref="users")

class RoomAl1(db.Model):
    __tablename__ = 'roomAl1'

    # uname = db.Column(db.String(255), nullable=False)
    id = db.Column(db.Integer,primary_key=True)
    uname = db.Column(db.String(255), db.ForeignKey('users.username'), nullable=False)
    sentence = db.Column(db.String(255), nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)
