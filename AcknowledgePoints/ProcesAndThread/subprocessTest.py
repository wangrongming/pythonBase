#!/usr/bin/dev python3
#-*-coding:utf-8-*-
import subprocess
#subprocess.call(["cat","subprocessTest.py"])
#��ν�linux����Ľ�����͵���ʾ��
p = subprocess.Popen(["ls","-all"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
text = p.stdout.read().decode()
#print(text)

#����ӽ��̻���Ҫ���룬�����ͨ�� communicate()��������
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\exit\n')
print(output.decode('utf-8'))

print('Exit code:', p.returncode)
print('err',err.decode('utf-8'))