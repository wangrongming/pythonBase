#!/usr/bin/dev python3
#-*-coding:utf-8-*-

#全局变量修改必须加锁
#局部变量只有线程自己看见，无需要加锁，传递起来麻烦
#如果一层一层传递：麻烦  如果定义一个全局变量的话：每个线程处理不同的student对象，不能共享
#创建全局ThreadLocal对象
#解决了 参数在一个线程中 ，各个函数之间互相传递的问题
import threading
# 创建全局 ThreadLocal 对象:
local_school = threading.local()
def process_student():
    #获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
    
def process_thread(name):
    # 绑定 ThreadLocal 的 student:
     local_school.student = name
     process_student()
t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()