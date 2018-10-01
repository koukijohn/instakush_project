#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
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


@app.route('/')
def instakush_home(the_id=None):
    """
    handles request to custom template with states, cities & amentities
    """
    cache_id = "?" + str(uuid.uuid4())
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    print (states)
    return render_template('instakush.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=cache_id)

if __name__ == "__main__":
    """
    MAIN Flask App"""
app.run(host=host, port=port)
