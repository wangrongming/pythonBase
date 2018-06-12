#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""使用requests请求代理服务器
请求http适用网页适用，不适用请求https网页
"""

import requests
import base64

#要访问的目标网页
page_url = "http://dev.kuaidaili.com/testproxy"

proxy = "106.14.220.153:16816"

#用户名和密码(私密代理/独享代理)
username = "1768389896"
password = "1psm8vc6"

proxies = { 'http': 'http://%s' % proxy, }

headers = {
    "Accept-Encoding": "Gzip", #使用gzip压缩传输数据让访问更快
    "Proxy-Authorization": "Basic %s" % base64.b64encode(b'%s:%s' % (username, password)), #不需要验证(如开放代理)，就不带这个header
}

r = requests.get(page_url, proxies=proxies, headers=headers)

print(r.status_code) #获取Reponse的返回码

if r.status_code == 200:
    r.enconding = "utf-8" #设置返回内容的编码
    print(r.content) #获取页面内容