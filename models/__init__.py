#!/usr/bin/python3
'''
    Package initializer
'''

from models.base_model import BaseModel
from models.user import User
from models.driver import Driver
from models.dispensary import Dispensary
from models.item import Item
from models.order import Order
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


classes = {"User": User, "BaseModel": BaseModel,
           "Driver": Driver, "Dispensary": Dispensary,
           "Item": Item, "Order": Order}

if getenv('instakush_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
