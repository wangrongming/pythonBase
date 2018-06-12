#proxy pool acknowledge point

1
#flask 
#source url https://blog.csdn.net/geekleee/article/details/52505605
from flask import render_template #使用jinja模板
from flask import Flask
app = Flask(__name__)

__all__ = ['app']# __all__ 提供了暴露接口用的”白名单“

@app.route('/post/<string:name>')
def show_post(name):
    #return 'Post %d' % post_id 
    user = {'nickname':name}
    return render_template('index.html',title='Home',user=user)
if __name__=='__main__':
    app.run()
'''
这就是传说中的MVC：Model-View-Controller，中文名“模型-视图-控制器”。 
Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等； 
包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。 
MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。 

{{}}表示这是一个变量，可以根据用户在模块端给予的参数的不同，进行调整
{% %}这样代表控制语句，eg:{% if title %}意思是如果有传入title变量，则显示title-microblog
{% extends "base.html" %} #通过这句话，来进行继承挂钩，和主体base.html进行链接
'''

2
#redis key-value数据库

#window下安装
Redis-x64-xxx.zip#下载安装包
redis-server.exe redis.windows.conf#运行 redis路径加入系统环境变量 redis.windows.conf 可省略
redis-cli.exe -h 127.0.0.1 -p 6379 #新开窗口 切换到redis目录下运行
    
#ubuntu下安装：
    sudo apt-get install redis-server
    redis-server#启动redis
    redis-cli#打开客户端
    redis commond
    #链接客户端
    redis-cli -h 127.0.0.1 -p 6379 -a "mypass"
    set 'a' 'b'
    get 'a'
    sudo vi /etc/redis/redis.conf     requirepas myredisserver
    service redis restart
    redis-cli -a myredisserver
#redis用法（第一个元素为下标0、-1表示最后一个元素）
self._db.lrange("proxies", 0, count - 1)#返回一个列表，包含指定区间内的元素(闭区间)。
self._db.ltrim("proxies", count, -1)# 对一个列表进行修剪(trim)，就是说，让列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除。执行成功返回OK
self._db.rpush("proxies", proxy) #将一个或多个值插入到列表的尾部(最右边)。 返回列表长度
self._db.rpop("proxies").decode('utf-8')#移除并返回列表的最后一个元素。  列表的最后一个元素。 当列表不存在时，返回 nil 。
self._db.llen("proxies")#get length from queue. Redis Llen 命令用于返回列表的长度。 如果列表 key 不存在，则 key 被解释为一个空列表，返回 0 。 如果 key 不是列表类型，返回一个错误。
_db.flushall()#flush db 清空整个 Redis 服务器的数据(删除所有数据库的所有 key )
DBSIZE#返回当前数据库的 key 的数量。
conn.pop
url/
3
#元类
定义模板类,集成type(),
定义我们需要的类:metaclass=模板类名称

__new__()方法接收到的参数依次是：
1. 当前准备创建的类的对象；
2. 类的名字；
3. 类继承的父类集合；(tuple)
4. 类的方法集合。(dict)

4
#格式化函数
str.format()
"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序

5
#生成器 两种写法
#g = (x * x for x in range(10))
#。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
FreeProxyGetter 用途 get_raw_proxies


6
#报错如何处理
pip install fake-useragent
fake-useragent 将收集到的数据缓存到temp文件夹, 例如 /tmp, 更新数据:
from fake_useragent import UserAgent
ua = UserAgent()
ua.update()
有时候会因为网络或者其他问题,出现异常(fake_useragent.errors.FakeUserAgentError: Maximum amount of retries reached), 可以禁用服务器缓存(从这里踩了一个坑, 没仔细看文档的锅):
from fake_useragent import UserAgent
ua = UserAgent(use_cache_server=False)
可以自己添加本地数据文件(v0.1.4+)
import fake_useragent

# I am STRONGLY!!! recommend to use version suffix
location = '/home/user/fake_useragent%s.json' % fake_useragent.VERSION

ua = fake_useragent.UserAgent(path=location)
ua.random



7
#异步下载 异步io
asyncio 是 Python 3.4 版本引入的标准库，直接内置了对异步 IO 的支持。
asyncio 的编程模型就是一个消息循环。我们从 asyncio 模块中直接获取
一个 EventLoop 的引用，然后把需要执行的协程扔到 EventLoop 中执行，
就实现了异步 IO。
