import redis
from Demo4ProxyPool.proxypool.error import PoolEmptyError
from Demo4ProxyPool.proxypool.setting import HOST,PASSWORD,PORT

class RedisClient(object):
    def __init__(self):
        if PASSWORD:
            self._db = redis.Redis(host=HOST,port=PORT,password=PASSWORD)
        else:
            self._db = redis.Redis(host=HOST,port=PORT)
    def get(self,count=1):
        """
                get proxies from redis
                """
        proxies = self._db.lrange("proxies", 0, count - 1)#返回列表中制定取件内的元素 0，0返回第一个
        self._db.ltrim("proxises",count,-1)#修剪 只保留指定区间内的元素
        return proxies

    def put(self,proxy):
        """
               add proxy to right top
               """
        self._db.rpush("proxies",proxy)#将一个或多个值插入到列表尾部

    def pop(self):
        """
        get proxy from right.
        """
        try:
            return self._db.rpop("proxies").decode('utf-8')#移除并返回列表的最后一个元素
        except:
            raise PoolEmptyError

    @property
    def queue_len(self):
        """
        get length from queue.
        """
        return self._db.llen("proxies")

    def flush(self):
        """
        flush db
        """
        self._db.flushall()#清空整个 Redis 服务器的数据(删除所有数据库的所有 key )

if __name__ == '__main__':
    conn = RedisClient()
    # print(conn.put('mingming'))
