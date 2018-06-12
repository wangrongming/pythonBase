import  socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定要监听的端口
s.bind(('127.0.0.1',9999))
#开始监听端口 指定等待连接的最大数量
s.listen(5)
print('wait for connection....')

def tcplink(sock,addr):
    print(addr)
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello,%s!' % data).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)

while True:
    #接受一个新连接
    sock,addr = s.accept()
    #创建一个新线程处理tcp连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()



