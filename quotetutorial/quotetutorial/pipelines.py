# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#处理item数据
import pymongo
from scrapy.exceptions import DropItem

class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        return item
        # if item['text']:
        #     if len(item['text']) > self.limit:
        #         item['text'] = item['text'][0:self.limit].rstrip()+'...'
        #     return item
        # else:
        #     return DropItem('Missing Text')

class MongoPipeline(object):

    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    #类方法 和类进行交互，但不和其实例进行交互的函数方法
    #相对与在类外定义一个方法  放到类的内部与类进行交互

    #拿到一些全局的配置 对当前类的初始化参数进行赋值
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    #程序启动的时候 执行这个操作
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self,item,spider):
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self):
        self.client.close()