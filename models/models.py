from PORTFOLIO.database import db
from sqlalchemy.orm import relationship

class Login(db.Model):
    __tablename__ = 'login'

    id = db.Column(db.Integer,primary_key=True)
    uname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    users = db.relationship("User", uselist=False, backref="login")

class Signup(db.Model):
    __tablename__ = "signup"
    
    id = db.Column(db.Integer,primary_key=True)
    uname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    users = db.relationship("User", uselist=False, backref="login")


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(20), nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)