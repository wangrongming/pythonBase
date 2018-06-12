from flask import Flask, request, render_template
import pymysql
import datetime

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    row = queryOne(username,password)
    if int(row) >= 1:
        row = query()
        return render_template('signin-ok.html', username=username,list=row)
    return render_template('form.html', message='Bad username or password', username=username)
#新增
def conn():
    #创建连接
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='',db='test',charset='utf8')
    #创建游标
    return conn

@app.route('/insert', methods=['GET'])
def insertGet():
    return render_template('insert.html')
@app.route('/insert', methods=['POST'])
def insert():
    name = request.form['username']
    password = request.form['password']
    print(name)
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='', db='test', charset='utf8')
    cursor = conn.cursor()
    a = cursor.execute("insert into user(name,password)values('%s','%s')" % (name,password))
    conn.commit()
    cursor.close()
    conn.close()
    return render_template("success.html")

@app.route('/delete', methods=['POST'])
def delete():
    name = request.form['username']
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='', db='test', charset='utf8')
    cursor = conn.cursor()
    a = cursor.execute("delete from user where name = '%s'" % name)
    conn.commit()
    cursor.close()
    conn.close()
    row = query()
    if a > 1:
        return render_template('signin-ok.html', message='删除成功', list=row)
    else:
        return render_template('signin-ok.html', message='删除失败', list=row)

def queryOne(name,password):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='', db='test', charset='utf8')
    cursor = conn.cursor()
    row = cursor.execute("select name,password from user where name='%s' and password='%s' " % (name,password))
    return str(row)

def query():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='', db='test', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select name,password from user")
    list = cursor.fetchall()
    return list
    # for li in list:
    #     print(li[0],li[1])


if __name__ == '__main__':
    app.run()
    # insert('haohao','123456')
    # query()
    print('nihoa')
