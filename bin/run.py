__author__ = 'uruddarraju'

from celeryflask.api.v1.startup import blueprint as startup
from flask import Flask

app = Flask(__name__, static_url_path='')

app.register_blueprint(startup)