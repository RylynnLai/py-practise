#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests, re
from bs4 import BeautifulSoup
from biplist import *


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

r = requests.get("http://music.baidu.com/top/new/?pst=shouyeTop")

soup = BeautifulSoup(r.content, "html.parser")

#获得歌曲列表
# musicArr = soup.body.find_all(attrs={"data-film":"null"})
musicArr = soup.body.find_all('div', class_='song-item')

musicList = []

for contentStr in musicArr:
    keywordSpan = contentStr.find('span', class_='song-title ')
    singerSpan = contentStr.find('span', class_='singer')

    keyword = keywordSpan.a.attrs['title']
    singer = singerSpan.span.attrs['title']
    name = keyword.replace(singer, '')

    dic = {'singer':singer,'name':name,'keyword':keyword}
    songDic = {'data':dic}
    # songDic = {'data':dic}

    handleDic = {}

    if handleSongDic(dic, handleDic):
        songDic['handleData'] = handleDic
        pass

    musicList.append(songDic)
    pass


#写入plist文件    
try:
    writePlist({'musicList':musicList}, 'musicList.plist')
    pass
except (InvalidPlistException,NotBinaryPlistException), e:
    print "fail to write plist Something bad happened:",e
    raise
else:
    pass
finally:
    pass


