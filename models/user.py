#!/usr/bin/python3
'''
    Class representing a lesson
'''
from models.base_model import BaseModel
import models
import os

class User(BaseModel):
    '''
        Definition of the Lesson class
    '''
    name = ''
    address = ''
    username = ''
    password = ''
    phone = ''