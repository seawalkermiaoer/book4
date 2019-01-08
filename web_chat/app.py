# -*- coding:utf-8 -*-
# __author__ = 'xianghai'

from gevent.pywsgi import WSGIServer

from flask import Flask
from flask import render_template
from flask_restful import Api
from gevent.pywsgi import WSGIServer
from flask_cors import CORS

from web_chat.qa import SmartQA

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


if __name__ == '__main__':
	CORS(app, supports_credentials=True)
	# 同义词更新
	api = Api(app)
	api.add_resource(SmartQA, "/qa")
	WSGIServer(("0.0.0.0", 8888), app).serve_forever()
