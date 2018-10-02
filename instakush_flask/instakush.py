#!/usr/bin/python3
"""
Flask App that integrates with instakush static HTML Template
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid

# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 7777
host = '0.0.0.0'


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route('/home')
def instakush_home(the_id=None):
    """
    handles request to custom template with
    """
    cache_id = "?" + str(uuid.uuid4())
    dispensary = storage.all('Dispensary').values()
    item = storage.all('Item').values()
    return render_template('instakush_home.html',
                           dispensary=dispensary,
                           item=item,
                           cache_id=cache_id)

@app.route('/drivers')
def instakush_drivers(the_id=None):
    """
    template for instakush driver infrastructure
    """
    cache_id = "?" + str(uuid.uuid4())
    drivers = storage.all('Driver').values()
    return render_template('instakush_drivers.html',
                           drivers=drivers,
                           cache_id=cache_id)

@app.route('/dispensary')
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

@app.route('/dispensary/<the_id>/items')
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
                           cache_id=cache_id)

if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
