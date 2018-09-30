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

class Order(BaseModel, Base):
    '''
        Definition of the Lesson class
    '''
    __tablename__ = 'order'
    mode = Column(String(128), nullable=False)
    user_id = Column(String(128), nullable=False)
    dispensary_id = Column(String(128), nullable=False)
    item_id = Column(String(128), nullable=False)
