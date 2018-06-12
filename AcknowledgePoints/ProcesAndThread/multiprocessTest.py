#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing import Process
import os

#�ӽ���Ҫִ�еĴ���
def run_proc(name):
    print('Run child process %s(%s)' % (name,os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('TCP',))
    print('Child process will start.')
    p.start()
    p.join()
    print('child process end')