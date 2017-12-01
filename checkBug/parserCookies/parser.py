#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*- coding: UTF-8 -*-  


def parserCooliiesStr(str):
    arr = str.split(';')
    dic = {}
    for s in arr:
        keyValues = s.split('=')
        dic[keyValues[0].lstrip().rstrip()] = keyValues[1].lstrip().rstrip()
        pass
    pass
    return dic