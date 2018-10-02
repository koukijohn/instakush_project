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

class Location(BaseModel, Base):
    '''
        Definition of the Location class
    '''
    __tablename__ = 'location'
    dispensary_id = Column(String(128), nullable=False)
    lat = Column(String(128), nullable=False)
    lon = Column(String(128), nullable=False)
    