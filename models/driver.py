#!/usr/bin/python3
'''
    Class representing a Driver
'''
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import os

class Driver(BaseModel, Base):
    '''
        Definition of the Lesson class
    '''
    __tablename__ = 'driver'
    name = Column(String(128), nullable=True)
    location = Column(String(128), nullable=True)
    username = Column(String(128), nullable=True)
    password = Column(String(128), nullable=True)
    marks = Column(String(128), nullable=True)
