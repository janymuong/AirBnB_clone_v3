#!/usr/bin/python3
'''module api/v1/views/__init__.py:
creates a Blueprint instance with `url_prefix` set to `/api/v1`
register the routes for app_views
'''
from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
