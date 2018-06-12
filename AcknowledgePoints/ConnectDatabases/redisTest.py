#!/usr/bin/env python
# -*- coding:utf-8 -*-


#redis数据库环境安装（维护爬取队列）
#redis.msi 文件github直接下载运行
#redis可视化界面安装：RedisDesktopManager

#redis是一个key-value存储系统
#数据都是缓存在内存中
#Redis 是一个高性能的key-value数据库

#python操作redis
#1、连接方式
import redis
# r = redis.Redis(host='127.0.0.1',port=6379,db=0)
# r.set('name','zhangsan') #默认不存在则创建，存在则修改
# print(r.get('name'))

#redis操作命令 linux
sudo apt-get install redis-server
sudo apt-get install redis-cli
# sudo vi /etc/redis/redis.conf
sudo service redis
bind 127.0.0.1
requirepass myredisserver
sudo service redis restart
redis-cli -a myredisserver


#2、连接池
#建立一个连接池，然后作为Redis的参数，这样就可以实现多个Redis实例共享一个连接池。
pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
r=redis.Redis(connection_pool=pool)
# r.set('name','lisi')
# print(r.get('name'))

        ########################################1、String 操作
        #批量设置值
        # r.mset(name1='zhangsan', name2='lisi')
        #批量获取
        # print(r.mget("name1","name2"))
        #
        # #根据字节获取子序列
        # r.set("name","zhangsan")
        # print(r.getrange("name",0,3))#输出:zhan
        # #修改字符串内容，从指定字符串索引开始向后替换，如果新值太长时，则向后添加
        # r.set("name","zhangsan")
        # r.setrange("name",1,"z")
        # print(r.get("name")) #输出:zzangsan
        # #在name对应的值后面追加内容
        # r.set("name","zhangsan")
        # print(r.get("name"))    #输出:'zhangsan
        # r.append("name","lisi")
        # print(r.get("name"))    #输出:zhangsanlisi
        ########################################2、list 操作
        # 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
        # r.lpush("list_name",2)
        # r.lpush("list_name",3,4,5)#保存在列表中的顺序为5，4，3，2
        print(r.llen('list_name'))
        #移除列表的左侧第一个元素，返回值则是第一个元素
        print(r.lpop("list_name"))
        #根据索引获取列表内元素
        # print(r.lindex("list_name",1))
        #分片获取元素
        print(r.lrange("list_name",0,-1))

        ########################################3、其他常用操作
        print(r.delete('list_name'))
        #根据name删除redis中的任意数据类型
        print(r.exists('list_name'))
        #检测redis的name是否存在
#4、管道
#redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
# 如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，
# 并且默认情况下一次pipline 是原子性操作。

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
pool = redis.ConnectionPool(host='192.168.0.110', port=6379)
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

r.set('name', 'zhangsan')
r.set('name', 'lisi')

pipe.execute()

#5 发布和订阅
#首先定义一个RedisHelper类，连接Redis，定义频道为monitor，定义发布(publish)及订阅(subscribe)方法。
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import redis
class RedisHelper(object):
    def __init__(self):
        self.__conn = redis.Redis(host='192.168.0.110', port=6379)  # 连接Redis
        self.channel = 'monitor'  # 定义名称

    def publish(self, msg):  # 定义发布方法
        self.__conn.publish(self.channel, msg)
        return True

    def subscribe(self):  # 定义订阅方法
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub

#发布者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#发布
from RedisHelper import RedisHelper
obj = RedisHelper()
obj.publish('hello')#发布

#订阅者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#订阅
from RedisHelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()#调用订阅方法

while True:
    msg= redis_sub.parse_response()
    print (msg)