#!/usr/bin/dev python3
#-*-coding:utf-8-*-

#ȫ�ֱ����޸ı������
#�ֲ�����ֻ���߳��Լ�����������Ҫ���������������鷳
#���һ��һ�㴫�ݣ��鷳  �������һ��ȫ�ֱ����Ļ���ÿ���̴߳���ͬ��student���󣬲��ܹ���
#����ȫ��ThreadLocal����
#����� ������һ���߳��� ����������֮�以�ഫ�ݵ�����
import threading
# ����ȫ�� ThreadLocal ����:
local_school = threading.local()
def process_student():
    #��ȡ��ǰ�̹߳�����student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
    
def process_thread(name):
    # �� ThreadLocal �� student:
     local_school.student = name
     process_student()
t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()