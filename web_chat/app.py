# -*- coding:utf-8 -*-
# __author__ = 'xianghai'
import json
import urllib.parse

import sys

import os
from pprint import pprint

from gevent.wsgi import WSGIServer

import requests
from flask import Flask, request
from flask import render_template
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


if __name__ == '__main__':
	WSGIServer(("0.0.0.0", 8888), app).serve_forever()
