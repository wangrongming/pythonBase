python简单登录
WSGI：Web Server Gateway Interface:Web服务器网关接口
    def application(environ, start_response):
     start_response('200 OK', [('Content-Type', 'text/html')])
     return [b'<h1>Hello, web!</h1>']
     environ：一个包含所有 HTTP 请求信息的 dict 对象；
     start_response：一个发送 HTTP 响应的函数。
Python 内置了一个 WSGI 服务器，这个模块叫 wsgiref
#使用web框架
常用web框架

 Django：全能型 Web 框架；
 web.py：一个小巧的 Web 框架；
 Bottle：和 Flask 类似的 Web 框架；
 Tornado：Facebook 的开源异步 Web 框

#MVC模型
Python 处理 URL 的函数就是 C：
Controller 负责业务逻辑，比如检查用户名是否存在，取出用户信息等等

Model 是用来传给 View 的，这样 View 在替换
变量的时候，就可以从 Model 中取出相应的数据

Jinja2，其中模版使用的 jinja2 模版
包含变量{{ name }}的模板就是 V：View，View 负责显示逻辑，通过简
单地替换一些变量，View 最终输出的就是用户看到的 HTML。

 模版一定要放到templates 目录下
 增加删除查找
 
#mysql操作
msyqld -install

sc delete mysql
net start msyql
mysql -u root -p
alter user 'root'@'localhost' identified by '123456';
alter user 'root'@'localhost' identified  by '123456';
flush privileges
quit
#安装mysqldb
pip install PyMySQL

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `password` varchar(40) NOT NULL,
  `date` DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



   
 
    


