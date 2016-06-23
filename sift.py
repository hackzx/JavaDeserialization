# encoding: utf-8
# 自動從apache的日誌中篩選請求「shell.jar」的IP。
# 然後嘛，批量上「jdexp.py」啦。

import os
import re

os.system('cat /var/log/apache2/* | grep shell.jar > /tmp/tmp')
# if os.path.exists('')
file = open("/tmp/tmp")

for line in file.readlines():
        p = r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])'
        ip = re.findall(p, line)
        ip = ''.join(ip) # change list to str
        iplist = '/tmp/iplist'
        f = open(iplist, 'a')
        f.write(ip+'\n')
        f.close()

if os.path.exists('/tmp/iplist'):
	os.system('cat /root/JavaDeserialization/iplist /tmp/iplist |sort |uniq >/tmp/tmp')
	os.remove('/root/JavaDeserialization/iplist')
	os.system('mv /tmp/tmp /root/JavaDeserialization/iplist')
else:
	print "ERROR: 没有找到请求shell.jar的IP。"

if os.path.exists('/tmp/iplist'):
	os.remove('/tmp/iplist')

print "\n JavaDeserialization\'s IP List: \n"
os.system('cat /root/JavaDeserialization/iplist')
print "\r"