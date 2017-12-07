#!/usr/bin/python
# -*- coding: utf-8 -*-

import kugou, getBaiduMusicList2
from biplist import *

fileName =  getBaiduMusicList2.getMusicList()

try:
    dic = readPlist(fileName)
    pass
except (InvalidPlistException,NotBinaryPlistException), e:
    print "fail to read plist Something bad happened:",e
    raise
else:
    pass
finally:
    pass

lists = dic['musicList']
mList = []
for item in lists:
	mList.extend(item)
	pass

num = 0
nump = 0

unmatchingList = []
print '开始匹配酷狗曲库...'
for song in mList:
	# print song['singer']+ song['name']+ song['keyword']
	data = song['data']
	flag = kugou.searchSong(data['singer'].encode('utf-8'), data['name'].encode('utf-8'), data['keyword'].encode('utf-8'))
	if flag:
		num += 1
		pass
	else:
		dic = {'singer':data['singer'], 'name':data['name']}
		print '匹配失败:' + data['keyword'].encode('utf-8')
		if len(song) > 1:
			print '有原版本,继续匹配...'
			flag = kugou.searchSong(song['handleData']['singer'].encode('utf-8'), song['handleData']['name'].encode('utf-8'), song['handleData']['keyword'].encode('utf-8'))
			if flag:
				nump += 1
				dic['o'] = 1
				pass
			else:
				dic['o'] = 0
				print '原版本匹配失败'
			pass
		unmatchingList.append(dic)
		pass
	pass

print '%d首完全成功共%d, 包括原版共成功%d' % (len(mList), num, num + nump)
writePlist({'unmatchingList':unmatchingList}, fileName + '匹配失败目录.plist')