from PORTFOLIO.database import db
from sqlalchemy.orm import relationship

class Login(db.Model):
    __tablename__ = 'login'

    id = db.Column(db.Integer,primary_key=True)
    # firstname = db.Column(db.String(50), nullable=False)
    # lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    users = db.relationship("User", uselist=False, backref="login")


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(255), nullable=False)
    lname = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)

class RoomAl1(db.Model):
    __tablename__ = 'roomAl1'

    id = db.Column(db.Integer,primary_key=True)
    sentence = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
