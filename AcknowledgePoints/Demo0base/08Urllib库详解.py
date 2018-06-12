#urllib是什么
#python内置的HTTP请求库（后续会用requests代替）
    #urllib.request 请求模块
    #urllib.error 异常处理模块
    #urllib.parse url解析模块
    #urllib.robotparser robot.txt解析模块（确定那些内容可以爬取  那些内容不可以爬取）

#urllib eg:
    #get类型请求
        # import urllib.request
        # response = urllib.request.urlopen('http://www.baidu.com')
        # print(response.read().decode('utf-8'))
    #post请求(httpbin.org)
        #data = bytes(urllib.parse.urlencode({'word':'hello'})),encoding='utf-8')
        #response = urllib.request.urlopen('http://httpbin.org/post',data=data)
    #超时设置
        # response = urllib.request.urlopen('http://www.baidu.com',timeout=0.1)

#request
    from urllib import request,parse
    url = "http://httpbin.org/post"
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host':'httpbin.org'
    }
    dict = {
        'name':'Germey'
    }
    data = bytes(parse.urlencode(dict),encoding='utf-8')
    req = request.Request(url=url,data=data,headers=headers,method='POST')
    response = request.urlopen(req)

#handler
#代理
import urllib.request
proxy_handler = urllib.request.ProxyHandler({
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://www.baidu.com')

#cookie
import http.cookiejar,urllib.request
cookie = http.cookiejar.Cookiejar()
opener = urllib.request.HTTPCookieProcessor(cookie)
response = open.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)

#异常处理
from urllib import request,error
try:
    response = request.urlopen('http://cuiqingcai.com/index.html')
except error.HTTPError as e:#404 urlerror子类 网络是连通的，请求不正确
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:#即没有连接到指定的服务器
    print(e.reason)
else:
    print('request successfully')

#URL解析 urlparse
from urllib.parse import urlparse
request = urlparse('http://www.baidu.com/index.html#comment',allow_fragments=False)
print(request)
#ParseRequest(scheme='http',netloc='www.baidu.com',path='/index.html#commmet',params='',query='',fragment='')

#urlunparse
from urllib.parse import urlunparse
data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))
#http://www.baidu.com/index.html;user=?a=6#comment

#urljoin 拼接url
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com','FAQ.html'))

#urlencode
from urllib.parse import urlencode
params = {
    'name':'Tom',
    'age':22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

#urllib.robots.txt





