#!/usr/bin/python3
'''
    Class representing a lesson
'''
from models.base_model import BaseModel
import models
import os

class Driver(BaseModel):
    '''
        Definition of the Lesson class
    '''
    name = ''
    location = ''
    username = ''
    password = ''
    marks = ''