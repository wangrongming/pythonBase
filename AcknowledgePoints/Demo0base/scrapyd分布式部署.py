#scrapyd 分布式

#redis去重 
    Redis集合中存储每个Request的指纹
    在向Request队列中加入Request前首先验证Request指纹是否已经添加到集合中了
    如果已经存在，不添加到队列
    不存在，添加到队列
#防止中断：启动判断
    在每台从机scrapy启动时都会首先判断当前RedisRequest队列是否为空
    如果不为空,则从队列中取得下一个Request执行爬取
    如果为空重新开始爬取，第一台从机执行爬取向队列中添加Request

#Scrapyd_redis
    #源码 https://github.com/rolando/scrapy-redis/
    pip install scrapy_redis
    
#爬取知乎
    
