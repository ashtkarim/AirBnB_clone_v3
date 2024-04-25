#!/usr/bin/python3
"""
INDEX
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def getStatus():
    return jsonify({"status": "OK"})
