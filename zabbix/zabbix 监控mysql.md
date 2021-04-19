## zabbix模板监控，测试于4.0
### 脚本文件
```
#!/bin/bash
# -------------------------------------------------------------------------------
# FileName:    check_mysql.sh
# Revision:    1.0
# Date:        2015/06/09
# Author:      DengYun
# Email:       dengyun@ttlsa.com
# Website:     www.ttlsa.com
# Description: 
# Notes:       ~
# -------------------------------------------------------------------------------
# Copyright:   2015 (c) DengYun
# License:     GPL

# 主机地址/IP
MYSQL_HOST=$1


MYSQL_PORT=$2

# 用户名
MYSQL_USER=$3

# 密码
MYSQL_PWD=$4

# 数据连接
MYSQL_CONN="/usr/bin/mysqladmin -u${MYSQL_USER} -p${MYSQL_PWD} -h${MYSQL_HOST} -P${MYSQL_PORT}"
# 参数是否正确
if [ $# -ne "5" ];then 
    echo "arg error!" 
fi 

# 获取数据
case $5 in 
    Uptime) 
        result=`${MYSQL_CONN} status 2>/dev/null|cut -f2 -d":"|cut -f1 -d"T"` 
        echo $result 
        ;; 
    Com_update) 
        result=`${MYSQL_CONN} extended-status 2>/dev/null|grep -w "Com_update"|cut -d"|" -f3` 
        echo $result 
        ;; 
    Slow_queries) 
        result=`${MYSQL_CONN} status 2>/dev/null|cut -f5 -d":"|cut -f1 -d"O"` 
        echo $result 
        ;; 
    Com_select) 
        result=`${MYSQL_CONN} extended-status 2>/dev/null|grep -w "Com_select"|cut -d"|" -f3` 
        echo $result 
                ;; 
    Com_rollback) 
        result=`${MYSQL_CONN} extended-status 2>/dev/null|grep -w "Com_rollback"|cut -d"|" -f3` 
                echo $result 
                ;; 
    Questions) 
        result=`${MYSQL_CONN} status 2>/dev/null|cut -f4 -d":"|cut -f1 -d"S"` 
                echo $result 
                ;; 
    Com_insert) 
        result=`${MYSQL_CONN} extended-status 2>/dev/null|grep -w "Com_insert"|cut -d"|" -f3` 
                echo $result 
                ;; 
    Com_delete) 
        result=`${MYSQL_CONN} extended-status 2>/dev/null|grep -w "Com_delete"|cut -d"|" -f3` 
                echo $result 
                ;; 
    Com_commit) 
        result=`${MYSQL_CONN} extended-status 2>/dev/null|grep -w "Com_commit"|cut -d"|" -f3` 
                echo $result 
                ;; 
    Bytes_sent) 
        result=`${MYSQL_CONN} extended-status 2>/dev/null|grep -w "Bytes_sent" |cut -d"|" -f3` 
                echo $result 
                ;; 
    Bytes_received) 
        result=`${MYSQL_CONN} extended-status 2>/dev/null|grep -w "Bytes_received" |cut -d"|" -f3` 
                echo $result 
                ;; 
    Com_begin) 
        result=`${MYSQL_CONN} extended-status 2>/dev/null|grep -w "Com_begin"|cut -d"|" -f3` 
                echo $result 
                ;; 
                        
        *) 
        echo "Usage:$0(Uptime|Com_update|Slow_queries|Com_select|Com_rollback|Questions|Com_insert|Com_delete|Com_commit|Bytes_sent|Bytes_received|Com_begin)" 
        ;; 
esac
```

### 修改agent配置文件
```
vi /usr/local/zabbix/etc/zabbix_agentd.conf
    Include=/etc/zabbix/zabbix_agentd.d/*.conf
```
### 创建mysql配置文件
```
vi /etc/zabbix/zabbix_agentd.d/userparameter_mysql.conf 
    UserParameter=mysql.version,mysql -V
    UserParameter=mysql.status[*],/etc/zabbix/zabbix_agentd.d/script/check_mysql.sh $1 $2 $3 $4 $5
    UserParameter=mysql.ping[*],mysqladmin -h$1 -P$2 -u$3 -p$4 ping 2>/dev/null| grep -c alive
```

### 模板见DB#Mysql
    注意填写宏
    如果想要便捷，方便运维工程师添加监控，则所有的mysql都使用zabbix-server主机上的agent，只需要在页面配置宏即可
    ps:也不排除用户提供的账号只能在localhost访问，如此只能在数据库服务器上安装agent
    再ps:由于5.7之后安全策略问题，命令行直接输入密码会warning，且无法过滤。因此在所有命令后追加 2>/dev/null，将错误日志转储，同时也会过滤掉其它的日志，检查时注意

### 重启服务
```
    service zabbix_agentd restart
```

****
由于zabbix自带模板只有14个监控项，又试了下percona
[教程来源](https://blog.csdn.net/mchdba/article/details/51447750)
脚本，模板来源
```	
    wget https://www.percona.com/downloads/percona-monitoring-plugins/1.1.6/percona-zabbix-templates-1.1.6-1.noarch.rpm
```

模板解压后，用管理页面导入

安装
```
	rpm -ivh percona-zabbix-templates-1.1.6-1.noarch.rpm
```

>ps:我用的是2.0的server，导入模板是不需要修改。最新的server需要修改模板来兼容，或者找到别人修改过的模板。这里没有具体去看

    复制 userparameter_percona_mysql.conf到被监控的agent下
	cp /var/lib/zabbix/percona/templates/userparameter_percona_mysql.conf /usr/local/zabbix/etc/zabbix_agentd.conf.d/

### 修改zabbix_agentd.conf
```
	vim /etc/zabbix/zabbix_agentd.conf
	    Include=/etc/zabbix/zabbix_agentd.d/    userparameter_percona_mysql.conf       
```
### 修改脚本
```
	vim /var/lib/zabbix/percona/scripts/get_mysql_stats_wrapper.sh
	    RES=`/usr/bin/mysql -e 'SHOW SLAVE STATUS\G' | egrep '(Slave_IO_Running|Slave_SQL_Running):' | awk -F: '{print $2}' | tr '\n' ','`    

    vim /var/lib/zabbix/percona/scripts/ss_get_mysql_stats.php
        mysql_user = 'zabbixmoniter';
        mysql_pass = 'ys_ipowerlong0418';
        mysql_port = 3306;
```

重启服务

server端测试
```
    zabbix_get -s 127.0.0.1 -p10050 -k "MySQL.Threads-connected"
    zabbix_get -s 127.0.0.1 -p10050 -k "MySQL.Handler-commit"
```

测试监控slave配置
```
	sh /var/lib/zabbix/percona/scripts/get_mysql_stats_wrapper.sh running-slave
```

如果提示没有密码
```
	vi /etc/my.cnf
	    [mysql]
	    user=***
	    password=***
	    #socket=/var/lib/mysql/mysql.sock #socket不确认要加
```

>如果提示权限不足，如
 	Access denied; you need the SUPER,REPLICATION CLIENT privilege for this operation
先进入mysql下，这里我试着直接用root用户填到my.cnf，居然不行。这里赋权用其它用户登录没有测试，不过自己给自己赋更高权权理论上就行不通吧？
	mysql -uroot -p***
	GRANT SELECT, PROCESS, SUPER, REPLICATION CLIENT ON *.* TO user'@'localhost' IDENTIFIED BY "password";     
	flush privileges;
然后再测试就ok了



>另，以上步骤不确定是否全部需要，此外还有步骤我没有用，比如创建用户以及修改端口的需求我没有。
还可以参考https://www.cnblogs.com/kevingrace/p/6256395.html