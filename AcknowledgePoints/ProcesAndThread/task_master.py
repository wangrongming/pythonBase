#!/usr/bin/dev python3
#-*-coding:utf-8-*-
#�첽IO
#�� Thread �� Process �У�Ӧ����ѡ Process���� Process ���ȶ�
#Process ���Էֲ�����̨�����ϣ��� Thread ���ֻ�ֲܷ���ͬһ̨�����Ķ�� CPU ��

#�ѷ�������Ľ��̺ʹ�������Ľ��̷ֲ�����̨������
#master/workerģ��

import random,time,queue
from multiprocessing.managers import BaseManager

# ��������Ķ���:
task_queue = queue.Queue()
# ���ս���Ķ���
result_queue = queue.Queue()

# �� BaseManager �̳е� QueueManager:
class QueueManager(BaseManager):
    pass
# ������ Queue ��ע�ᵽ������, callable ���������� Queue ����:
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)
# �󶨶˿� 5000, ������֤��'abc':
manager = QueueManager(address=('',5000),authkey=b'abc')
#���� Queue:
manager.start()
# ���ͨ��������ʵ� Queue ����:
task = manager.get_task_queue()
result = manager.get_result_queue()
# �ż��������ȥ:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
    
# �� result ���ж�ȡ���:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# �ر�:
manager.shutdown()
print('master exit.')

