from . import db
from datetime import datetime


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    email = db.Column(db.String(255),unique = True,index = True)
    password = db.Column(db.String(255), nullable=False)

    # def __repr__(self):
    #     return f"{self.name}"


class Meta(db.Model):

    id = db.Column(db.Integer,primary_key =True)
    
    def __repr__(self):
        return f"{self.username}"

class Role(db.Model):

    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(255))
    user_id = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

class Drives(db.Model):

    id = db.Column(db.Integer,primary_key =True)
    vaccination = db.Column(db.String,nullable=False)
    date = db.Column(db.DateTime,nullable=False)
    location = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return f"Drives {self.vaccination}"

class Detail(db.Model):

    __tablename__ = 'details'
    id = db.Column(db.Integer,primary_key =True)
    child_name = db.Column(db.String(255))
    child_age = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    def save_detail(self):
        db.session.add(self)
        db.session.commit()
