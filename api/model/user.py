from sqlalchemy import Column, Integer, String, DateTime

from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    password = Column(String(100))
    email = Column(String(255), unique=True, nullable=False)
    registered_on = Column(DateTime, nullable=False)
