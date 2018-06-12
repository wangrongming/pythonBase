#!/usr/bin/dev python3
# -*-coding:utf-8-

# 异步 IO 模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程：
# loop = get_event_loop()
# while True:
# event = loop.get_event()
# process_event(event)
# 协程
# Coroutine。
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行
# 是一个线程执行的

# 协程：子程序切换不是线程切换，程极高的执行效率，不需要多线程的锁机制，因为只有一个线程

# yield 不但可以返回一个值，它还可以接收调用者发出的参数

# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，？？？？？？？？？？？？？

def consumer():
    r = ''
    while True:
        n = yield r  # 这里程序返回
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)

# c.send(None)启动生成器；
# 2. 然后，一旦生产了东西，通过 c.send(n)切换到 consumer 执行；
# 3. consumer 通过 yield 拿到消息，处理，又通过 yield 把结果传回；
# 4. produce 拿到 consumer 处理的结果，继续生产下一条消息；
# 5. produce 决定不生产了，通过 c.close()关闭 consumer，整个过程结shu
# “子程序就是协程的一种特例。