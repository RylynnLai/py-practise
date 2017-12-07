#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, json, re, sys
from biplist import *

reload(sys)
sys.setdefaultencoding('utf8')

url= 'http://tingapi.ting.baidu.com/v1/restserver/ting?format=json&calback=&from=webapp_music&method=baidu.ting.billboard.billList&type=2ß&size=100&offset=%d'
offsetNum = 0
hasMore = 1
fileName = 'temp'

#去除括号及其内容
def handleString(str):
    out = re.sub('([\(|（][\s\S]+?[\)|）])', '', str)
    return out
    pass

def handleSongDic(dic, handleDic):
    singer = handleString(dic['singer'])
    name = handleString(dic['name'])
    keyword = handleString(dic['keyword'])

    if singer != dic['singer'] or name != dic['name'] or keyword != dic['keyword']:
        handleDic['singer'] = singer
        handleDic['name'] = name
        handleDic['keyword'] = keyword
        return 1
        pass
    else:
        return 0
        pass
    pass


def requestMusicList(offset):
	r = requests.get(url % offset)
	dic = json.loads(r.content)

	try:
		tempList = dic['song_list']
		global fileName 
		global hasMore 

		# 保存日期名字,只保存第一次请求
		if offsetNum == 0:
			fileName = dic['billboard']['update_date']
			pass

		musicList = []
		for item in dic['song_list']:
			tempDic = {'singer':item['author'],'name':item['title'],'keyword':item['author'] + item['title']}
			songDic = {'data':tempDic}

			# print item['title']
			handleDic = {}

			if handleSongDic(tempDic, handleDic):
				songDic['handleData'] = handleDic
				pass

			musicList.append(songDic)
			pass
		return {'musicList':musicList, 'hasMore':dic['billboard']['havemore']}
		pass
	except Exception as e:
		print 'json缺少字段------'
		print r.url
		print '----------'
		raise e
	pass

def getMusicList():
	global offsetNum 
	global fileName 
	global hasMore
	musicList = []

	print '获取今天百度热歌榜'
	while 1:
		listDic = requestMusicList(offsetNum)
		print '加载第%d个...%d' % (offsetNum, len(listDic['musicList']))
		musicList.append(listDic['musicList'])
		offsetNum += 100

		if not hasMore: break
		hasMore = listDic['hasMore']
		pass

	fileName = fileName + '热歌榜' 
	print '结束,写入plist文件:' + fileName + '.plist'
	#写入plist文件    
	writePlist({'musicList':musicList}, fileName + '.plist')
	return fileName + '.plist'
	pass

# getMusicList()


