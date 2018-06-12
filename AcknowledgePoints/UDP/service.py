import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))
#直接接收来自任何客户端的数据
print('Bind up on 9999')
while True:
    data,addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello,%s' % data,addr)
