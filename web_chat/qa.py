from flask import request
from flask_restful import Resource
from web_chat.get_tuling import get_chatting


class SmartQA(Resource):
	
	def __del__(self):
		pass
	
	def post(self):
		try:
			text = request.form["text"]
			print(text)
			return {"succ": True, "text": get_chatting(text)}, 200
		except Exception as e:
			print(e)
			return {"text": "error while qa", "succ": False}, 200

