#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*- coding: UTF-8 -*-  

import requests, os, time
from parserCookies import parser
from bs4 import BeautifulSoup


session = requests.Session()
user_login, url_bugs = 'http://172.17.21.16/zentao/user-login.html', 'http://172.17.21.16/zentao/my-bug-assignedTo.html'


def checkBugs():
    r = session.get(url_bugs)

    # 指定报文编码格式
    r.encoding = requests.utils.get_encodings_from_content(r.text)[0]

    soup = BeautifulSoup(r.text, "html.parser")

    if soup.tfoot:
        divs = soup.tfoot.find_all('div')
        if divs[1].string == '暂时没有记录':
            print(divs[1].string)
            return 0
            pass
        else:
            os.system('open -a /Applications/Safari.app http://172.17.21.16/zentao/my-bug.html')
            return 1
        pass
    else:
        print('cookies过期，登录已失效')
        return -1
    pass

def login():
    print('请依次输入账号密码')
    username = input("账号：")
    pwd = input('密码：')
    para = {'account':username, 'password':md5(pwd)}

    r = session.post(user_login, data = para)

    return r.status_code == requests.codes.ok
    pass

def md5(str):
    import hashlib
    m = hashlib.md5()   
    m.update(str.encode("utf8"))
    return m.hexdigest()

login()
while 1:
    result = checkBugs()
    if result == 0:
        time.sleep(5)
    elif result == 1:
        break
    elif result == -1:
        while login() == 0: #登录失败
            pass
        print('登录成功')
        pass






