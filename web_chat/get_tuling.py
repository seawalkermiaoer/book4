# -*- coding:utf-8 -*-
# __author__ = 'seawalker'
import requests


def get_chatting(content):
	rsp = requests.get("http://www.tuling123.com/openapi/api?key=49de46c409c047d19b2ed2285e8775a6&info=" + content)
	rsp.json()
	
# {"code":100000,"text":"你陪我玩我就好啦"}
if __name__ == '__main__':
	get_chatting("你好")
