#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from biplist import *
	
def readUsers():
	try:
		path = os.getcwd() + '/temp'
		plist = readPlist(path + '/users.plist')
		return plist['users']
		
	except InvalidPlistException, e:
		print "Not a Plist or Plist Invalid:",e
    

def runClone():
	users = readUsers()
	for user in users:
		if int(user['num']) > 0:
			
			
			pass
		pass