# coding: utf-8

# URLError

from urllib import request, error

'''
try:
    response = request.urlopen('http://www.chiyi.com.cn/index.htm')
except error.URLError as e:
    print(e.reason)

# HTTPError 是URLError的子类，专门用来处理HTTP请求错误，比如认证请求失败等
# 有code, reason, headers三个属性
'''

try:
    response = request.urlopen('http://www.chiyi.com.cn/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')

import socket

try:
    response = request.urlopen('http://www.baidu.com', timeout=0.01)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('Time out')
