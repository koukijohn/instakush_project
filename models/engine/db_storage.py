#!/usr/bin/python3
'''
    DBStorage Engine
'''

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from os import getenv
from models import base_model, user, driver, dispensary, item, order, location
from models.user import User
from models.driver import Driver
from models.dispensary import Dispensary
from models.item import Item
from models.order import Order
from models.location import Location


class DBStorage:
    '''
        DBStorage Class
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        Initializes DBStorage class
        '''
        # get values from environment variables
        user = getenv('instakush_MYSQL_USER')
        password = getenv('instakush_MYSQL_PWD')
        host = getenv('instakush_MYSQL_HOST')
        database = getenv('instakush_MYSQL_DB')
        # establish db connection
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        # create tables with metadata
        Base.metadata.create_all(self.__engine)
        # special case for testing
        if getenv('instakush_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Session = sessionmaker(self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        '''
        Query on the current database session all objects
        depending of the class name.
        '''
        all_objects = {}
        if type(cls) == str:
            cls = eval(cls)
        if cls is None:
            obj_list = [User, Driver, Dispensary, Item, Order, Location]
            for cls in obj_list:
                for obj in self.__session.query(cls).all():
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    all_objects[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                all_objects[key] = obj
        return(all_objects)

    def new(self, obj):
        '''
        Add the object to the current database session.
        '''
        self.__session.add(obj)

    def save(self):
        '''
        Commit all changes of the current database session.
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        Deletes obj from db.
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''
        Create all tables in the database and
        create the current database session.
        '''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session

    def close(self):
        '''
            This will close remove() method on the private session attribute
            (self.__session) or close() on the class.
        '''
        self.__session.close()
