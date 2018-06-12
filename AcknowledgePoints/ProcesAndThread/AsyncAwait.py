#!/usr/bin/dev python3
# -*-coding:utf-8-

# Python 从 3.5 版本开始
# 1. 把@asyncio.coroutine 替换为 async；
# 2. 把 yield from 替换为 await。
import asyncio
import threading


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")


# 获取 EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行 coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()