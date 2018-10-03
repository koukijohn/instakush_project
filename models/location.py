#!/usr/bin/python3
'''
    Class representing our Location
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
    dispensary_id = Column(String(128), nullable=True)
    name = Column(String(128), nullable=True)
    lat = Column(String(128), nullable=True)
    lon = Column(String(128), nullable=True)
    img_link = Column(String(128), nullable=True)
