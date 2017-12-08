#!/usr/bin/python
# -*- coding: utf-8 -*-

import kugou, getBaiduMusicList2
from biplist import *

path = '/home/pi/py/plists/'

fileName =  getBaiduMusicList2.getMusicList()

try:
    dic = readPlist(path + fileName)
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
	# print song['singers']+ song['name']+ song['keyword']
	data = song['data']
	flag = kugou.searchSong(data['singers'], data['name'], data['keyword'])
	if flag:
		num += 1
		pass
	else:
		dic = {'singers':data['singers'], 'name':data['name']}
		print '匹配失败:' + data['keyword'].encode('utf-8')
		if len(song) > 1:
			print '有原版本,继续匹配...'
			flag = kugou.searchSong(song['handleData']['singers'], song['handleData']['name'], song['handleData']['keyword'])
			if flag:
				nump += 1
				dic['原版匹配结果'] = 1
				pass
			else:
				dic['原版匹配结果'] = 0
				print '原版本匹配失败'
			pass
		unmatchingList.append(dic)
		pass
	pass

n1 = num * 100.0 / len(mList)
n2 = (num + nump) * 100.0 / len(mList)

print '%d首完全成功共%d--%f%%, 包括原版共成功%d--%f%%' % (len(mList), num, n1, num + nump, n2)



writePlist({'unmatchingList':unmatchingList}, path + fileName + '匹配失败目录.plist')

