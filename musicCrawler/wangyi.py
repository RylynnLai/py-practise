#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, os
from biplist import *

searchUrl = 'http://music.163.com/api/search/get/'

cookies = {"appver":"2.0.2"}
data = {"s":"薛之谦骆驼","limit":"20", "type":"1", "offset":"0"}

r = requests.post(searchUrl, data=data ,cookies = cookies)



print r.content