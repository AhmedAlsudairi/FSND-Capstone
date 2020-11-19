from sqlalchemy import Column, String, create_engine, Date, Integer
from flask_sqlalchemy import SQLAlchemy
import json
import os
database_path = os.environ['DATABASE_URL']

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

  def __init__(self, title, release_date=""):
    self.title = title
    self.release_date = release_date

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date}

class Actor(db.Model):  
  __tablename__ = 'Movie'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  age = Column(Integer, nullable=False)
  gender = Column(String, nullable=False)

  def __init__(self, name, age="", gender):
    self.name = name
    self.age = age
    self.gender = gender

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender}