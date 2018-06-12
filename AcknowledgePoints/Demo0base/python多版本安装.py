
#python多版本共存问题
    #windows
        #配置环境变量：c:python36;c://pyton36/scripts;
        #where python:寻找当前pytlhon的路径值有哪些  where pip:寻找pip有那些
        #将当前python.exe 复制为：python3.exe cmd窗口中输入 python3 只会运行python3
        #同理对 pip.exe 配置为：pip2.exe pip3.ext pip-conda.exe  pip-conda-scripts.py
        #异常：
            #unable to create using process:此时需要升级pip
            #python2 -m pip install --upgrade pip

    #linux
        #echo $path 跟window环境配置同理
        #whereis python2   whereis pyothon3 查找当前pythoh位置
        #建立软连接配置python 路径 ln -s /usr/bin/python3.5 /usr/bin/python3
        #删除软连接 rm -rf /usr/bin/python3
        #pip 配置同理

    #pycharm
        #setting:配置运行python版本

#爬虫常用库的安装过程
    #window
        #urllib re(默认自带库)
        #requests pip3 install requests
        #selenium pip3 install selenium
            #下载chromedriver 跟pip放在同一级目录下面
            #from selenium import webdriver
            # dirver=webdirver.Chrome()
            #dirve.get('http://www.baidu.com')
        #phantomjs 无界面浏览器 phantomjs.exe 下载 配置环境变量
            #phantomjs 直接进入
            #driver=webdirver.PhantomJS()
        #lxml pip install lxml  pip install wheel(下载好wheel之后在页面安装 .whl文件)
            #pip3 install c:\download\lxml-3.7.3-cp36-cp36m-win_amd64.whl

        #beautifulsoup (依赖与lxml库) pip install beautifulsoup4
            #from bs4 import BeautifulSoup
            #soup = BeautifulSoup('<html></html>','lxml')
        #pyquery (相对与beautiful更方便) pip install pyquery
            #from pyquery import PyQuery as pq
            #doc = pq('<html>Hello</html>')
            #result = doc('html').text()
        #pymysql  pip install pymysql(python3) (mysqlpython python2)
        #pymongo pip install pymongo
        #redis pip install redis (公共的 分布式爬虫维护一个爬取队列)
        #flask pip install flask
            #import flask
        #django   web的一个框架，模版引擎，接口，路由（分布式爬虫的维护） pip instal django
            #import django
        #jupyter (notebook:记事本功能) pip install jupyter
            #jupyter notbook
    #linux
        #pip install request selenium beautifulsoup4 pyquery pymysql pymongo redis flask django jupyter


