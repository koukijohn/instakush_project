#!/usr/bin/python3
'''
    Class representing our Items
'''
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import os

class Item(BaseModel, Base):
    '''
        Definition of the Lesson class
    '''
    __tablename__ = 'item'
    strain = Column(String(128), nullable=False)
    img_link = Column(String(128), nullable=False)
    dispensary_id = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    price = Column(String(128), nullable=False)
    company = Column(String(128), nullable=False)
    serving_size = Column(String(128), nullable=False)
    stock = Column(String(128), nullable=False)
    cannabis_type = Column(String(128), nullable=False)
