#基于urllib，使用更加方便
#安装
    #pip install requests

#实例引入
import requests
response = requests.get('http://www.baidu.com')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)

#各种请求方式 get请求方式
import requests
data = {
    'name':'Tom',
    'age':22
}
response = requests.get('',params=data)
print(response.text)

#解析json
import json
#下面返回结果一样
print(response.json())
print(json.loads(response.text))

#获取二级制数据
    #response.content

#添加headers
heasers = {
    'User-Agent':''
}
response = requests.get('http://www.zhihu.com/expore',headers=heasers)

#基本post请求
data = {'name':'germey','age':'22'}
response = requests.post('http://httpbin.org/post',data=data)

#response属性


#高级操作
    #文件上传
    file = {'file':open('favcon.ico','rb')}
    response = requests.post("http://httpbin.org/post",files=file)
    print(response.text)
    #获取cookie
    for key,value in response.cookies.items():
        print(key,value)
    #会话维持
    import requests
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456')
    s.get('http://httpbin.org/cookies')
    print(response.text)

    #证书验证
    requests.get('http://www.12306.cn',verify=False)
    requests.get('http://www.12306.cn',cert=('/path/server.crt','/path/key'))

    #代理设置
    import requests
    proxies = {
        "http":"http://127.0.0.1:9743",
        "https":"https://127.0.0.1:9743"
    }
    response = requests.get("http://taobao.com",proxies=proxies)
    print(response.status_code)

    pip install 'request[socks]'
    proxies = {
        'http':'sock5://127.0.0.1:9742',
        'https':'sock5://127.0.0.1:9742'
    }
    response = requests.get("http://taobao.com", proxies=proxies)
    print(response.status_code)

    #超时设置
    response = requests.get("http://taobao.com", timeout=1)#必须在1秒时间内应答

    #认证设置（访问页面时候需要进行登录才可以）
    requests.get("http://taobao.com", auth=('user','123'))

#异常处理模块
    from requests.exceptions import ReadTimeout,ConnectionError,RequestException
    try:
        print('')
    except ReadTimeout  :
        pass
    except ConnectionError:
        pass
    except RequestException:
        pass



