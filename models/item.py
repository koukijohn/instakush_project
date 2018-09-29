#!/usr/bin/python3
'''
    Class representing a lesson
'''
from models.base_model import BaseModel
import models
import os

class Item(BaseModel):
    '''
        Definition of the Lesson class
    '''
    strain = ""
    img_link = ""
    dispensary_id = ""
    description = ""
    price = ""
    company = ""
    serving_size =""
    stock = ""
    cannabis_type = ""