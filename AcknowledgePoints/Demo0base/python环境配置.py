网易镜像源
http://mirrors.163.com/  
  python环境安装整理
第一节：环境搭建
    设置国内镜像源 pip(pip.ini文件)
    http://pan.baidu.com/s/1c21pU4S （外网观看）

###"自动化大本营 3m社区
python安装方法  
linux ubuntu环境的具体安装方法   
sudo apt-get install python3-dev 
sudo apt-get install bulid-essentail 
sudo apt-get install libssl 
sudo apt-get install libffi-dev 
sudo apt-get install libxml2 
sudo apt-get install libxml2-dev 
sudo apt-get install libxslt1-dev 
sudo apt-get install zlib1g-dev
sudo apt-get install python3
sudo apt-get install python-pip

##安装ssh
问题：secureCRT The remote system refused the connection
原因：IP地址冲突、服务没有启动
dpkg -l | grep ssh
ps -e|grep ssh #查看执行进程
重启 /etc/init.d/ssh restart
sudo apt-get install openssh-server
#更新软件源  更新软件列表  更新软件
1、备份文件
sudo cp /etc/apt/sources.list /etc/apt/sources.list.old
sudo apt-get update
sudo apt-get upgrade
##apt-get 更换阿里源
sudo vim /etc/apt/sources.list
ssh登录失败
##pip下载 更换阿里源
http://mirrors.aliyun.com/pypi/simple/
临时使用
pip3 install pillow -i https://mirrors.aliyun.com/pypi/simple/
永久修改：
~/.pip/pip.conf (没有就创建一个)， 内容如下：
index-url=https://mirrors.aliyun.com/pypi/simple/
#Ubuntu:root用户登录
设置root的密码
sudo passwd root
#ubuntu pip3安装
安装
sudo apt-get install python3-pip
升级
sudo pip3 install --upgrade pip
卸载
sudo apt-get remove python3-pip

#静态IP配置
    #enp0s3为网卡的名字不可以替换
auto enp0s3
iface enp0s3 inet static
address 192.168.1.101    
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameserver 119.29.29.29
    #同时重启网络
    重启网络：sudo /etc/init.d/networking restart
    sudo cat /etc/resolv.conf命令看DNS是否设置成功。 下面有自动生成的nameserver
1、熟练掌握爬虫requests、scrapy、爬虫流程，掌握正则表达式，xpath、css提取网页资源的方法
2、熟练构建分布式爬虫、Linux下定时启动爬虫
3、熟悉各个网站常见反爬策略，能根据网页分析出常见反爬手段
4、熟悉前端代码，可以分析目标网站真实requests地址和response内容
5、针对不同爬虫级别网站，做出具体scrapy配置,如：伪造User-Agent，批量IP代理池
6、使用日志，监控程序运行状况