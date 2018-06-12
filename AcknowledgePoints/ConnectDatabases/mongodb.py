#mongodb安装过程
#bin同层目录下新建data文件夹
#data文件夹新建db目录
#在bin目录下打开 dos窗口， mongod --dbpath c:\MongoDB\Server\3.4\data\db

#mongo:进入mongo客户端命令
db
db.test.insert(('a','b'))
db.test.get('a')

#mongodb配置成系统服务：
#新建data/logs/mongo.log文件
#mongod --bind_ip 0.0.0.0
#--logpath --c:\MongoDB\Server\3.4\data\logs\mongo.log --logappend --dbpath c:\MongoDB\Server\3.4\data\db
#--port 27017 --serviceName "MongoDB" --serviceDisplayName "MongoDB" --intall

#linux mongod
#sudo apt-get install mongod
#mongod
#mongo
#show dbs


#coding：utf-8
import pymongo
from pymongo import MongoClient
client = MongoClient()
client=MongoClient('10.0.0.9',27017)
#连接mongodb数据库
client=MongoClient('mongodb://127.0.0.1:27017/')
#指定数据库名称
db = client.test_database #use test_database
# print(db)
#获取非系统的集合
db.collection_names(include_system_collections=False)
#获取集合名
posts = db.posts
# print(posts)
#查找单个文档
doc = posts.find_one()
# print(doc)
#给定条件的一个文档
doc = posts.find_one({"author":"Eliot"})
# print(doc)
#根据id查找需要的ObjectID
from bson.objectid import ObjectId
post_id='5afb6489328a880d3c6fa431'
# document = client.db.collection.find_one({'_id':ObjectId(post_id)})
# print(document)
#插入多条记录
import datetime
new_posts=[{"author": "TOM","tags": ["bulk", "insert"],"date": datetime.datetime(2009, 11, 12, 11, 14)},
           {"author": "Mary",
            "title": "MongoDB is fun",
            "text": "and pretty easy too!",
            "date": datetime.datetime(2009, 11, 10, 10, 45)}]
# result = posts.insert_many(new_posts)
# print(result)
#返回插入的ID
# print(result.inserted_ids)

#递归集合
# for post in posts.find():
#     print(post)

#文档的记录数
# print(posts.count())

#区间查询
# db.col.find({likes : {$lt :200, $gt : 100}})
# 类似于SQL语句:Select * from col where likes>100 AND likes<200;
d = datetime.datetime(2008, 11, 12, 12)
# for post in posts.find({"date": {"$lt": d}}).sort("author"):
#     print(post)

##给集合profiles建立索引 唯一索引
# result = db.profiles.create_index([("user_id",pymongo.ASCENDING)],uniquw=True)
#查看索引信息
# print(list(db.profiles.index_information()))


user_profiles = [
{'user_id': 211, 'name': 'Luke'},
{'user_id': 212, 'name': 'Ziltoid'}]
# result = db.profiles.insert_many(user_profiles)
# db.profiles.remove({'name': 'Luke'})
#remove过时 使用 delete

#实际测试不能用delete
# db.profiles.deleteMany({})
# db.profiles.deleteMany({'name': 'Ziltoid'})
# db.profiles.deleteOne({'name': 'Ziltoid'})
print(list(db.profiles.find()))

