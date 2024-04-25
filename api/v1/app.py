#!/usr/bin/python3
""" Create new app """
from api.v1.views import app_views
from flask import Flask
from models import storage
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown(exception):
    """
    Handle close session
    """
    storage.close()


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else '0.0.0.0'
    port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)
