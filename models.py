from sqlalchemy import Column, String, create_engine, Date, Integer
from flask_sqlalchemy import SQLAlchemy
import json
import os
database_path = "postgres://cbqtrgconsrcct:281c3d25888c88e2a8ce66dd8030abe622d6cb349d0e3bc971f2495983185883@ec2-52-5-176-53.compute-1.amazonaws.com:5432/d30725h9f6sdpf"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Movie(db.Model):
    __tablename__ = 'Movie'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    roles = db.relationship('Role', backref=db.backref('movie', lazy=True))

    def __init__(self, title, release_date=""):
        self.title = title
        self.release_date = release_date

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date}

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()        

class Actor(db.Model):
    __tablename__ = 'Actor'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    roles = db.relationship('Role', backref=db.backref('actor', lazy=True))

    def __init__(self, name, gender, age=""):
        self.name = name
        self.age = age
        self.gender = gender

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender}

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()    

class Role(db.Model):
    __tablename__ = 'Role'

    movie_id = Column(Integer, db.ForeignKey('Movie.id'), primary_key=True)
    actor_id = Column(Integer, db.ForeignKey('Actor.id'), primary_key=False)
    name = Column(String, nullable=False)

    def __init__(self, movie_id, actor_id, name=""):
        self.movie_id = movie_id
        self.actor_id = actor_id
        self.name = name

    def format(self):
        return {
            'movie_id': self.movie_id,
            'actor_id': self.actor_id,
            'name': self.name}

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()    