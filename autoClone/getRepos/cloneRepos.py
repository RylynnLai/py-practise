#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, parserRepos
from biplist import *


def readUrls():
	path = os.getcwd() + '/temp'
	urls = []

	for x in xrange(0, 4):
		plistPath = path + '/Repo%d.plist' % x
		try:
			plist = readPlist(plistPath)
			urls.extend(plist['repos'])
			pass
		except InvalidPlistException, e:
			print "Not a Plist or Plist Invalid:",e
		pass

	if len(urls) > 0:
		return urls
		pass
	print '读取仓库失败'

def clone():
	path = os.getcwd() + '/repos'

	urls = readUrls()

	parserRepos.mkdir(path)
	os.chdir(path)

	for url in urls:
		os.system('git clone ' + url)
		pass
	pass
	






