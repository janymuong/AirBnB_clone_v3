#!/usr/bin/python3
'''module api/v1/views/index.py:
create a route `/status` on the object app_views
returns a jsonified response: 'status': 'OK'
'''

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def api_status():
    '''route:GET
    that returns a JSON response
    '''
    return jsonify({'status': 'OK'})
