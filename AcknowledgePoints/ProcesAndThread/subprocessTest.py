#!/usr/bin/dev python3
#-*-coding:utf-8-*-
import subprocess
#subprocess.call(["cat","subprocessTest.py"])
#如何将linux命令的结果不送到显示器
p = subprocess.Popen(["ls","-all"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
text = p.stdout.read().decode()
#print(text)

#如果子进程还需要输入，则可以通过 communicate()方法输入
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\exit\n')
print(output.decode('utf-8'))

print('Exit code:', p.returncode)
print('err',err.decode('utf-8'))