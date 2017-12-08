#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, requests, os, json, re

# searchUrl = 'http://songsearch.kugou.com/song_search_v2?callback=jQuery1124024729707568171322_1511860845824&keyword=%d&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1511860845863'
# searchUrl = 'http://songsearch.kugou.com/song_search_v2?keyword=%d&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1511860845863'
# url = 'http://so.service.kugou.com/get/complex?callback=jQuery1124024729707568171322_1511860845824&word=%E8%9D%8E%E5%AD%90%E4%B9%90%E9%98%9F&_=1511860845853'
searchUrl = 'http://songsearch.kugou.com/song_search_v2?platform=WebFilter&keyword='
serviceUrl = 'http://so.service.kugou.com/get/complex?word='
#命令行参数(歌手名字, 歌名, 关键字:一般为歌手+歌名)
singer = ''
name = ''
keyword = ''
if len(sys.argv) >= 3:
	singer = sys.argv[1]
	name = sys.argv[2]
	keyword = sys.argv[3]
	pass

#这个url可能是用于模糊搜索,暂时用不到
# def searchService(singer, name, keyword):
# 	if len(keyword) == 0:
# 		return 0
# 		pass
# 	print '开始搜索请求:' +  singer + '-' + name + '-' + keyword
# 	flag = 0
# 	r = requests.get(serviceUrl + keyword)

# 	result = r.text

# 	try:
# 		encodedjson = json.loads(result)
# 		pass
# 	except Exception as e:
# 		print '失败:' + r.content
# 		print r.url
# 		raise e

# 	if len(encodedjson['data']) > 0:
# 		print '搜索结果json解析成功'
# 		lists = encodedjson['data']['song']

# 		print '开始匹配------'
# 		for song in lists:
# 			title = song['singername'] + song['songname'] 
# 			if singer in title and name in title:
# 				flag = 1
# 				break
# 				pass
# 			pass
# 		pass
# 	else:
# 		print '失败:' + r.content
# 		print r.url
# 		pass
	
# 	return flag
# 	pass

def searchSong(singers, name, keyword):
	if len(keyword) == 0:
		return 0
		pass

	lists = searchSongWithKeyword(keyword)
	print '开始匹配...'
	for song in lists:
		title = song['FileName']
		if cmpKeyword(singers, name, title):
			print '匹配成功'
			return 1
			break
			pass
		pass

	lists = searchSongWithKeyword(name)
	for song in lists:
		title = song['FileName']
		if cmpKeyword(singers, name, title):
			print '匹配成功'
			return 1
			break
			pass
		pass
	
	return 0
	pass

def searchSongWithKeyword(keyword):
	print '开始搜索请求:' +  keyword
	
	r = requests.get(searchUrl + keyword)

	result = r.text

	try:
		encodedjson = json.loads(result)
		pass
	except Exception as e:
		print '失败:' + r.content
		print r.url
		raise e

	if len(encodedjson['data']) > 0:
		print '搜索结果json解析成功'
		return encodedjson['data']['lists']
		pass
	else:
		print '失败:' + r.content
		print r.url
		pass
	pass

#比较
def cmpKeyword(oSinger, oName, fileName):
	s2 = handleString(oName)
	s3 = handleString(fileName)

	s1 = 1
	for s in oSinger:
		if s not in fileName:
			s1 = 0
			break
			pass
		pass

	return s1 and s2 in s3
	pass

#去除中英文特殊标点,空格,字母全转小写
def handleString(str):
	string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", str)
	return string.lower()
	pass

# print(searchSong(singer, name, keyword))
# searchService(singer, name, keyword)






