from extensions import db
from sqlalchemy import Column, Integer, String
from db import Base


# Define the User model class.
class User(db.Model): 

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    password = db.Column(db.String(120), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    role = db.Column(db.String(50), nullable=False, default='user')

    phone = db.Column(db.String(20), nullable=True)

    address = db.Column(db.String(200), nullable=True)

    full_name = db.Column(db.String(100), nullable=True)