#!/usr/bin/python3
"""
er model for authentication service.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User class for representing the 'users' table in the database.
    
    Attributes:
        id (int): The user's ID (primary key).
        email (str): The user's email (non-nullable).
        hashed_password (str): The user's hashed password (non-nullable).
        session_id (str): The user's session ID (nullable).
        reset_token (str): The user's reset token (nullable).
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
