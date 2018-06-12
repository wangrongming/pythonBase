#!/usr/bin/dev python3
#-*-coding:utf-8-*
import time, sys, queue
from multiprocessing.managers import BaseManager
# �������Ƶ� QueueManager:
class QueueManager(BaseManager):
    pass
# ������� QueueManager ֻ�������ϻ�ȡ Queue������ע��ʱֻ�ṩ����
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# ���ӵ���������Ҳ�������� task_master.py �Ļ���:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# �˿ں���֤��ע�Ᵽ���� task_master.py ���õ���ȫһ��:
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
# ����������:
m.connect()
# ��ȡ Queue �Ķ���
task = m.get_task_queue()
result = m.get_result_queue()
# �� task ����ȡ����,���ѽ��д�� result ����:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

 #Queue ��������������������ͽ��ս����ÿ�����������������
#Ҫ����С����       