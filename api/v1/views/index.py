#!/usr/bin/python3
"""
INDEX
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", strict_slashes=False)
def getStatus():
    return jsonify({"status": "OK"})
