#!/usr/bin/python3
'''
    Class representing a lesson
'''
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import os

class User(BaseModel, Base):
    '''
        Definition of the Lesson class
    '''
    __tablename__ = 'user'
    name = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
