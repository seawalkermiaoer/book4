# -*- coding:utf-8 -*-
# __author__ = 'xianghai'

from gevent.wsgi import WSGIServer

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


if __name__ == '__main__':
	WSGIServer(("0.0.0.0", 8888), app).serve_forever()
