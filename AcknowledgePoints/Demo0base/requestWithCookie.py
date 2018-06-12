#/usr/bin/dev python3
#coding:utf-8
import io
import requests
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

url = 'https://weibo.cn/search/mblog?keyword=00001'
data = {
    'mp':'100',
    'page':'4',
}
headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '48',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'weibo.cn',
    'Cookie': '_T_WM=6724b6cb54676d80006facafe87c2433; SUB=_2A252E7SsDeThGeVP4lsW9yrFyTuIHXVV_9zkrDV6PUJbkdANLRjHkW1NTTxzvV-bOg7NV3Ap3spkxfzzGl0mppZS; SUHB=0tK61SpD1p29yV; SCF=AtoBJeLgQcN_xOuguNwoxBO2YIM1HsKo0Y3zLzFpWYZ59EdLQvZ2pxhzWWZTWIwqRN52IZCojQdXtxrrA3ABJs8.',
    'Origin': 'https://weibo.cn',
    'Referer': 'https://weibo.cn/search/?tf=5_012',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
response = requests.post(url,headers=headers,data=data)
print(response.status_code)`

