#!/usr/bin/python
# -*- coding: utf-8 -*-

import wangyi
from biplist import *

try:
    dic = readPlist('musicList.plist')
    pass
except (InvalidPlistException,NotBinaryPlistException), e:
    print "fail to read plist Something bad happened:",e
    raise
else:
    pass
finally:
    pass

lists = dic['musicList']
num = 0
nump = 0
print '开始匹配wangyi曲库...'
for song in lists:
	# print song['singer']+ song['name']+ song['keyword']
	data = song['data']
	flag = wangyi.searchSong(data['singer'].encode('utf-8'), data['name'].encode('utf-8'), data['keyword'].encode('utf-8'))
	if flag:
		num += 1
		pass
	else:
		print '匹配失败:' + data['keyword'].encode('utf-8')
		if len(song) > 1:
			print '有原版本,继续匹配...'
			flag = wangyi.searchSong(song['handleData']['singer'].encode('utf-8'), song['handleData']['name'].encode('utf-8'), song['handleData']['keyword'].encode('utf-8'))
			if flag:
				nump += 1
				pass
			else:
				print '原版本匹配失败'
			pass
		pass
	pass

print '%d首完全成功共%d, 包括原版共成功%d' % (len(lists), num, num + nump)