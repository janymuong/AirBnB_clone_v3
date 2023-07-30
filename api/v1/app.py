#!/usr/bin/python3
'''module api/v1/app.py:
create Flask app; and register the blueprint app_views to Flask instance app
'''

from os import getenv
from flask import Flask

from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_engine(exception):
    '''TearDown:
    closes the storage on app context teardown
    removes the current SQLAlchemy Session object after each request
    '''
    storage.close()


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = getenv('HBNB_API_PORT', 5000)
    app.run(host=HOST, port=PORT, threaded=True)
