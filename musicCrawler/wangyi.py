#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, os, sys, json, re
from biplist import *

searchUrl = 'http://music.163.com/api/search/get/'
cookies = {"appver":"2.0.2", "referer":"http://music.163.com"}


#命令行参数(歌手名字, 歌名, 关键字:一般为歌手+歌名)
singer = ''
name = ''
keyword = ''
if len(sys.argv) >= 3:
	singer = sys.argv[1]
	name = sys.argv[2]
	keyword = sys.argv[3]
	pass


def searchSong(singer, name, keyword):
	if len(keyword) == 0:
		return 0
		pass

	lists = searchSongWithKeyword(singer)
	print '开始匹配...'
	for song in lists:
		title = song['name']
		artist = song['artists'][0]['name']
		if cmpKeyword(singer, name, (title + artist).encode('utf-8')):
			if song['copyrightId']>1:
				print '匹配成功'
				return 1
				break
				pass
			pass
		pass

	lists = searchSongWithKeyword(name)
	print '开始匹配...'
	for song in lists:
		title = song['name']
		artist = song['artists'][0]['name']
		if cmpKeyword(singer, name, (title + artist).encode('utf-8')):
			if song['copyrightId']>1:
				print '匹配成功'
				return 1
				break
				pass
			pass
		pass

	lists = searchSongWithKeyword(singer + ' ' + name)
	print '开始匹配...'
	for song in lists:
		title = song['name']
		artist = song['artists'][0]['name']
		if cmpKeyword(singer, name, (title + artist).encode('utf-8')):
			print song['copyrightId']
			if song['copyrightId']>1:
				print '匹配成功'
				return 1
				break
				pass
			pass
		pass
	
	return 0
	pass

def searchSongWithKeyword(keyword):

	print '开始搜索请求:' +  keyword
	data = {"s":keyword,"limit":"100", "type":"1", "offset":"0"}

	r = requests.post(searchUrl, data=data ,cookies = cookies)

	try:
		encodedjson = json.loads(r.text)
		pass
	except Exception as e:
		print '失败:' + r.content
		print r.url
		raise e

	if encodedjson['code'] == 200:
		print '搜索结果json解析成功'
		return encodedjson['result']['songs']
		pass
	else:
		print '失败:' + r.content
		print r.url
		pass

	pass

#比较
def cmpKeyword(oSinger, oName, fileName):
	s1 = handleString(oSinger)
	s2 = handleString(oName)
	s3 = handleString(fileName)
	print s1 + ' ' + s2 + ' ' + s3 
	print oSinger + ' ' + oName + ' ' + fileName
	return s1 in s3 and s2 in s3
	pass

#去除中英文特殊标点,空格,字母全转小写
def handleString(str):
	string = re.sub("[\(\)\（\）\《\》\——\；\，\。\“\”\<\>\！]", "", str)
	return string.lower()
	pass

# lists =  searchSongWithKeyword('鹿晗 追梦赤子心')
# for x in lists:
# 	print x
# 	pass
print searchSong('鹿晗', '追梦赤子心', '鹿晗 追梦赤子心')