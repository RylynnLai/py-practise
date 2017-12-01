#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, json, requests, time
from biplist import *


url = 'https://m.10010.com/NumApp/NumberCenter/qryNum?callback=jsonp_queryMoreNums&sysCode=mall&provinceCode=51&cityCode=510&searchValue=&codeTypeCode=&net=01&goodsNet=4&searchCategory=3&judgeType=1&qryType=02&groupKey=85260254&_=1512003276272'

def handleNum(dic):
	arr = dic['numArray']

	count = len(arr) / 12
	lists = [] 
	for x in xrange(1,count):
		n = 12 * (x - 1)
		lists.append(arr[n:n+12])
		pass

	newLists = []
	# for item in lists:
	# 	s = item[0]
	# 	subStr = str(s)[3:11]
	# 	if '3' in subStr or '4' in subStr:
	# 		break
	# 		pass
	# 	else:
	# 		newLists.append(item)
	# 	pass
	return lists
	pass


def getNum():
	r = requests.get(url)

	jsonStr = r.text

	jsonStr = jsonStr.replace(jsonStr[0:20], '')
	jsonStr = jsonStr.replace(')', '')
	jsonStr = jsonStr.replace(';', '')

	# print jsonStr
	dic = json.loads(jsonStr)
	return dic

	pass

# # dic = getNum()
# print handleNum(getNum())

arr = []
count = 1000
while count >0:
	count -= 1
	print count
	try:
		arr.append(handleNum(getNum()))
		pass
	except Exception as e:
		writePlist({'data':arr},'num.plist')
		raise
	else:
		pass
	finally:
		pass
	pass

try:
    writePlist({'data':arr},'num.plist')
    pass
except (InvalidPlistException,NotBinaryPlistException), e:
    print "fail to write plist Something bad happened:",e
    raise
else:
    pass
finally:
    pass
