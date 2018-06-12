#!/usr/bin/dev python3
# -*-coding:utf-8-

# asyncio 是 Python 3.4 版本引入的标准库，直接内置了对异步 IO 的支持
# asyncio 的编程模型就是一个消息循环。
import asyncio
import threading


@asyncio.coroutine  # 把一个 generator 标记为 coroutine 类型，
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # 异步调用 asyncio.sleep(1):
    r = yield from asyncio.sleep(1)  # yield from 语法可以让我们方便地调用另一个 generator。
    # 当 asyncio.sleep()返回时，线程就可以从 yield from 拿到返回值（此处是 None）
    print('Hello again! (%s)' % threading.currentThread())


# 获取 EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行 coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 1. 把@asyncio.coroutine 替换为 async；
# 2. 把 yield from 替换为 await。