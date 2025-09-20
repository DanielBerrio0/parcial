from sqlalchemy import Column, Integer, String
from models.db import Base


# Define the User model class.
class User(Base): 

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    address = Column(String(200), nullable=True)
