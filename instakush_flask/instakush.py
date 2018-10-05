#!/usr/bin/python3
"""
Flask App that integrates with instakush static HTML Template
"""
from flask import Flask, render_template, url_for, jsonify
from models import storage
import uuid
import json
import requests


# flask setup
application = Flask(__name__)
application.url_map.strict_slashes = False
port = 7777
host = '0.0.0.0'


# begin flask page rendering
@application.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()

@application.route("/")
def instakush_login(the_id=None):
    """                                                                         
    handles request to custom template with                                     
    """
    cache_id = "?" + str(uuid.uuid4())
    return render_template('instakush_login.html')


@application.route("/tweets")
def instakush_tweets(the_id=None):
    """                                                                                            
    handles request to custom template with                                                        
    """
    cache_id = "?" + str(uuid.uuid4())
    return render_template('instakush_tweets.html')


@application.route('/strains')
def instakush_strains(the_id=None):
    """                                                                                        
    handles request to custom template with                                                    
    """
    cache_id = "?" + str(uuid.uuid4())
    response = requests.get("https://api.otreeba.com/v1/strains?sort=-createdAt").json()
    return render_template('instakush_strains.html',
                           strains=response['data'],
                           cache_id=cache_id)


@application.route('/home')
def instakush_home(the_id=None):
    """
    handles request to custom template with
    """
    cache_id = "?" + str(uuid.uuid4())
    dispensary = storage.all('Dispensary').values()
    item = storage.all('Item').values()
    location = storage.all('Location').values()
    return render_template('instakush_home.html',
                           dispensary=dispensary,
                           item=item,
                           location=location,
                           cache_id=cache_id)

@application.route('/drivers')
def instakush_drivers(the_id=None):
    """
    template for instakush driver infrastructure
    """
    cache_id = "?" + str(uuid.uuid4())
    drivers = storage.all('Driver').values()
    return render_template('instakush_drivers.html',
                           drivers=drivers,
                           cache_id=cache_id)

@application.route('/dispensary')
def instakush_dispensary(the_id=None):
    """
    template for instakush dispensary infrastructure
    """
    cache_id = "?" + str(uuid.uuid4())
    drivers = storage.all('Driver').values()
    dispensary = storage.all('Dispensary').values()
    return render_template('instakush_dispensary.html',
                           dispensary=dispensary,
                           cache_id=cache_id)

@application.route('/dispensary/<the_id>/items')
def instakush_dispensary_items(the_id):
    """
    template for instakush dispensary items infrastructure
    """
    cache_id = "?" + str(uuid.uuid4())
    drivers = storage.all('Driver').values()
    dispensary = storage.all('Dispensary').values()
    item = storage.all('Item').values()
    return render_template('instakush_items.html',
                           dispensary=dispensary,
                           item=item,
                           the_id=the_id,
                           cache_id=cache_id)

if __name__ == "__main__":
    """
    MAIN Flask Application"""
    application.run(host=host, port=port)
