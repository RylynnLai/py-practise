#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys, requests
from bs4 import BeautifulSoup 
from biplist import *

#python在安装时，默认的编码是ascii，当程序中出现非ascii编码时，python的处理常常会报类似这样的错误。
#python没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。

reload(sys) 
sys.setdefaultencoding('utf8') 

#创建文件夹路劲
def mkdir(path):
    # 引入模块
    import os
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print path+' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
        return False

#保存Html文件
def getHtml(urlStr):
    
    cookies = dict(i_like_gogits='08042707a20e1848')
    r = requests.get(urlStr, cookies=cookies)

    return r.text


#解析用户列表
def parserHtml(htmlStr, pageIndex):
	
    path = os.getcwd() + '/temp'
	#读取html文本
    html = htmlStr

    if len(html) < 10:
		print '获取到的html太短'
		return
		pass
	#创建soup
	#构建一个 BeautifulSoup 对象需要两个参数，第一个参数是将要解析的 HTML 文本字符串，第二个参数告诉 BeautifulSoup 使用哪个解析器来解析 HTML。
	#解析器负责把 HTML 解析成相关的对象，而 BeautifulSoup 负责操作数据（增删改查）。”html.parser” 是Python内置的解析器，”lxml” 则是一个基于c语言开发的解析器，它的执行速度更快，不过它需要额外安装
    soup = BeautifulSoup(html, "html.parser")

	#匹配所有的tr标签
    trs = soup.tbody.find_all('tr')

    repos = []
    for tr in trs:
        #匹配所有的td标签
        tds = tr.find_all('td')

        userName = tds[1].string
        repoName = tds[2].string
        gitUrl = 'http://172.17.16.23:3000/%s/%s.git' % (userName, repoName)
        repos.append(gitUrl)
        pass


    try:
        print '解析到的仓库地址列表在:' + path + "/Repo%d.plist" % pageIndex
        writePlist({'repos':repos}, path + '/Repo%d.plist' % pageIndex)
        pass
    except (InvalidPlistException,NotBinaryPlistException), e:
        print "fail to write plist Something bad happened:",e
        raise
    else:
        pass
    finally:
        pass

def parserRepos():
    for x in xrange(0,4):
        urlStr = "http://172.17.16.23:3000/admin/repos?page=%d&q=" % x
        html = getHtml(urlStr)
        parserHtml(html, x)
        pass
    pass
         