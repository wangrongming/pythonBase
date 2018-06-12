import redis
db = redis.Redis(host='127.0.0.1',port='6379')
a = db.lrange("proxies",0,1)
print(a)
