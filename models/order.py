#!/usr/bin/python3
'''
    Class representing a lesson
'''
from models.base_model import BaseModel
import models
import os

class Order(BaseModel):
    '''
        Definition of the Lesson class
    '''
    mode = ""
    user_id = ""
    dispensary_id = ""
    item_id = ""