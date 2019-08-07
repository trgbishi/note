这个揉了很多东西进来，用了2天，即最终不是一套流程完美结束的
记一下，可以试错

zabbix_server已经安装好了
tomcat端jmx已经配好，端口 8099
jmx账号密码已知
tomcat在16机
java_gateway和zabbix_server都在28机

### 安装
```
    ./configure --prefix=/usr/local/zabbix_java_gateway-2.0.6 --enable-java
    make && make install
```

### 配置zabbix_java_gateway
```
vi /etc/zabbix/zabbix_java_gateway.conf
    LISTEN_IP="0.0.0.0"
    LISTEN_PORT=10052
    PID_FILE="/tmp/zabbix_java.pid" #这个好像是默认就有的的，不用配
    START_POLLERS=5
```

### 这个文件可能也要配一下，和上面一样，也可能不需要
```
    /usr/local/zabbix/sbin/zabbix_java/settings.sh
```

### 配置zabbix_server
```
    JavaGateway=127.0.0.1       //java网关地址，即server端ip地址
    JavaGatewayPort=10052            //java网关监听端口
    StartJavaPollers=5
```

### 开始service java_gateway
```
    service service java_gateway start
    service service java_gateway status
```

### 如果不行的话，再试试。我是这里跑通了的
```
    /etc/init.d/zabbix_java_gateway start
    service service java_gateway status
```

### 看看10052，即java_gateway有没有打开
### 理论上zabbix java gateway already running ，端口就应该打开了
```
netstat  -tunlp | grep java
```

### 重启zabbix server
```
service zabbix_server restart
```

>其实还有一个指令也能跑
>```
>    /etc/init.d/zabbix_server restart
>```


### web操作
创建主机，主机名要去tomcat所在的机器查看 jmx接口 ip为***.16  端口8099

模板是网上找的新的
然后在模板内各个项目内，要填用户名称和密码，所有的教程都没有提到这一点。
用户名密码一个一个输入的，另外可以在外面定义宏，这里的两个空就可以用宏代替。
