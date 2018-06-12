#net start mysql
#mysql -u root -p

#linux mysql配置
vi /etc/mysql/mysql.conf.d
bind 127.0.0.1 注释掉
sudo service mysql restart



#!/usr/bin/python
# -*- coding:utf-8 -*-
import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='',db='TCP',charset='utf8')
#创建游标
cursor = conn.cursor()
# 1************执行SQL，并返回收影响行数
# effect_row = cursor.execute("select * from user")
# print(effect_row)

#2***********获取查询数据
#查询第一行数据
# row1 = cursor.fetchone()
# print(row1)
# 获取剩余结果前n行数据
# row2 = cursor.fetchmany(3)
# print(row2)
# print(type(row2))
# 获取剩余结果所有数据
# row3 = cursor.fetchall()
# print(row3)


#3***********获取新创建数据自增ID
# effect_row = cursor.executemany("insert into user(name,password) values(%s,%s)",[("ff","123456")])
# print(effect_row)
#获取自增id
# print(cursor.lastrowid)

#4***********移动游标
# cursor.scroll(1,mode='relative') # 相对当前位置移动
# print(cursor.fetchone())
# cursor.scroll(1,mode='absolute') # 相对绝对位置移动
# print(cursor.fetchone())

# 5**********fetch数据类型:默认为元祖数据类型  修改为dict类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("select * from user")
print(cursor.fetchone())
# 提交，不然无法保存新建或者修改的数据
conn.commit()

#6**********执行参数化查询(防止sql注入)
row_count=cursor.execute("select user,pass from tb7 where user=%s and pass=%s",(user,passwd))
#sql="select user,pass from tb7 where user='%s' and pass='%s'" % (user,passwd) 此种拼接有风险

#7**********使用with简化连接过程
#  定义上下文管理器，连接后自动关闭连接
import pymysql
import contextlib
@contextlib.contextmanager
def mysql(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1', charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()
# 执行sql
with mysql() as cursor:
    print(cursor)
    row_count = cursor.execute("select * from tb7")
    row_1 = cursor.fetchone()
    print
    row_count, row_1

# 关闭游标
cursor.close()
## 关闭连接
conn.close()


