[参考zabbix中文社区，主要是有一些地方处理方式不同(不同的地方我做了修改），以及备份该资料](http://www.zabbix.org.cn/viewtopic.php?f=13&t=5&start=0)


> 安装环境
> CentOS 6.5_64bit

1.  安装组件

    yum install make mysql-server httpd php mysql-devel gcc net-snmp-devel curl-devel perl-DBI php-gd php-mysql php-bcmath php-mbstring php-xml -y

    useradd zabbix

2. 启动mysql
	service mysqld start

    [安装mysql](https://www.cnblogs.com/lvlv/p/4173107.html)
```    
    service mysqld  stop
    mysqld_safe --user=mysql --skip-grant-tables --skip-networking &
    mysql -u root mysql
    mysql> UPDATE user SET Password=PASSWORD('newpassword') where USER='root';
    mysql> FLUSH PRIVILEGES;
    mysql> quit
    service mysqld  restart
    mysql -uroot -p
    Enter password: <输入新设的密码newpassword>
```

3. 创建zabbix数据库
```
    Mysql> create database zabbix character set utf8;
    Mysql> grant all on zabbix.* TO zabbix@'localhost' identified by 'zabbixpass'; --授权本机通过账号zabbix密码zabbixpass访问数据库的所有权限
    Mysql> flush privileges;
```
4. 导入数据库sql
```
    cd zabbix-2.0.6/database/mysql
	mysql -h localhost -uroot -proot zabbix <schema.sql #这里应该用zabbix和zabbixpass来导入sql文件，由于root是管理员账号，所以本地可以直接用来连接

    mysql -h localhost -uroot -proot zabbix <images.sql #这里应该用zabbix和zabbixpass来导入sql文件
    mysql -h localhost -uroot -proot zabbix <data.sql #这里应该用zabbix和zabbixpass来导入sql文件
```
5. 调整当前时间
```
	date -R #查询当前系统时间
	date -s "2013-04-26 20:48:55" #如果查询的时间不对就做修改
```    
6. 编译安装
```
    ./configure --with-mysql --with-net-snmp --with-libcurl --enable-server --enable-agent --enable-proxy --enable-java --prefix=/usr/local/zabbix
    make && make install
```    
7. 添加端口
```
    vim /etc/services
        zabbix-agent 10050/tcp # Zabbix Agent
        zabbix-agent 10050/udp # Zabbix Agent
        zabbix-trapper 10051/tcp # Zabbix Trapper
        zabbix-trapper 10051/udp # Zabbix Trapper
```
8. 修改配置文件
```
    vi /etc/httpd/conf/httpd.conf
	    DirectoryIndex index.html index.html.var index.php
    vi /usr/local/zabbix/etc/zabbix_server.conf
        DBName=zabbix
        DBUser=zabbix #连接数据库的账号,与Mysql授权账号对应
        DBPassword=zabbixpass #连接数据库的密码，与Mysql授权账号的密码对应

    cp misc/init.d/fedora/core5/zabbix_server /etc/init.d/
    cp misc/init.d/fedora/core5/zabbix_agentd /etc/init.d/
    chmod 700 /etc/init.d/zabbix_*
    vim /etc/init.d/zabbix_server
        ZABBIX_BIN="/usr/local/zabbix/sbin/zabbix_server"
    vim /etc/init.d/zabbix_agentd
        ZABBIX_BIN="/usr/local/zabbix/sbin/zabbix_agentd"

```
9. 启动服务并设置开机启动
```
    /etc/init.d/zabbix_server start
    /etc/init.d/zabbix_agentd start 

    chkconfig zabbix_server on
    chkconfig zabbix_agentd on
```    
10. 修改php相关参数
```
    vi /etc/php.ini
        max_execution_time = 300
        max_input_time = 300
        date.timezone = PRC
        post_max_size = 32M

    /etc/init.d/httpd restart
```

11. 配置php文件
```
    cd zabbix-2.0.6
    cd frontends/
    cp -rf php /var/www/html/
    cd /var/www/html
    mv php zabbix
    chown -R zabbix:zabbix zabbix
```

12. 给apache赋zabbix目录的配置写入权限
    >[参考](https://blog.csdn.net/wudixingyunxingxing/article/details/56561620)

```
    chown -R apache:apache /var/www/html/zabbix
```


>原帖方案是按照网站提示，将zabbix.conf.php拷贝到/var/www/html/conf(其实>应该是zabbix）/目录下，但是往虚拟机传文件比较麻烦。
>
>登录http://ip/zabbix
>
>安装成功后，初始登录账号admin，密码zabbix
>这里不是之前配置的数据库的密码！！！而是zabbix初始密码



****
> 以下是agent的单独安装
    groupadd zabbix
    useradd zabbix -g zabbix

1. 编译安装
```
    ./configure --with-net-snmp --with-libcurl --enable-agent --enable-proxy --prefix=/usr/local/zabbix
    make && make install
```

2. 添加端口
```
    vim /etc/services
    zabbix-agent 10050/tcp # Zabbix Agent
    zabbix-agent 10050/udp # Zabbix Agent
    zabbix-trapper 10051/tcp # Zabbix Trapper
    zabbix-trapper 10051/udp # Zabbix Trapper
```

3. 修改配置文件
```
    cp misc/init.d/fedora/core5/zabbix_agentd /etc/init.d/
    chown -R zabbix:zabbix /etc/init.d/zabbix_*
    chmod 700 /etc/init.d/zabbix_*
    su - zabbix
    vim /etc/init.d/zabbix_agentd
        ZABBIX_BIN="/usr/local/zabbix/sbin/zabbix_agentd"
```

4. 启动服务并设置开机启动
```
    /etc/init.d/zabbix_agentd start
    chkconfig zabbix_agentd on
```