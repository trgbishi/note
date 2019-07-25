mysql版本：mysql  Ver 14.14 Distrib 5.1.73, for redhat-linux-gnu (x86_64) using readline 5.1
本来安装的8.0.16版本mysql，但是后yum install zabbix-server-mysql时依赖包mysql-libs是5.1.73与安装的版本冲突，解决不了，保险起见将mysql也更换成5.1.73
一方面我认为zabbix不会强制依赖版本这么低的mysql，但是没有解决这个问题的话以后还是先检查一下zabbix-server-myqsl具体需求的版本

6.0安装操作主要参考了https://www.cnblogs.com/Tang-Yuan/p/9842429.html
他是采用编译安装来解决zabbix server + agent + web  配合 yum解决各种依赖包
这次主要帮我解决的问题是1.yum安装下没有正常的web界面的问题 2.安装php5.6版本时，yum不知道具体名称的问题

mysql操作
    mysqladmin -u root password root           #设置数据库root密码，可选
    mysql -u root -p        #root用户登陆数据库
    CREATE DATABASE zabbix character set utf8 collate utf8_bin;       #创建zabbix数据库（中文编码格式）
    [不同版本的mysql sql不一样，以下根据实际情况二选一
    1).
    GRANT all ON zabbix.* TO 'zabbix'@'%' IDENTIFIED BY 'zabbix';  #授予zabbix用户zabbix数据库的所有权限，密码zabbix
    GRANT all ON zabbix.* TO 'zabbix'@'127.0.0.1' IDENTIFIED BY 'zabbix';  #授予zabbix用户zabbix数据库的所有权限，密码zabbix
    GRANT all ON zabbix.* TO 'zabbix'@'localhost' IDENTIFIED BY 'zabbix';  #授予zabbix用户zabbix数据库的所有权限，密码zabbix
    2).
    create user 'zabbix'@'%' identified by 'zabbix';
    create user 'zabbix'@'localhost' identified by 'zabbix';
    create user 'zabbix'@'127.0.0.1' identified by 'zabbix';
    GRANT all ON zabbix.* TO 'zabbix'@'%' ;  #授予zabbix用户zabbix数据库的所有权限
    GRANT all ON zabbix.* TO 'zabbix'@'127.0.0.1' ;  #授予zabbix用户zabbix数据库的所有权限
    GRANT all ON zabbix.* TO 'zabbix'@'localhost' ;  #授予zabbix用户zabbix数据库的所有权限
    ]
    flush privileges;    #刷新权限
    quit                 #退出数据库   





Zabbix 3需要PHP是至少5.4或更高版本
    rpm -ivh http://repo.webtatic.com/yum/el6/latest.rpm

安装需要的包
    yum -y install httpd php56w php56w-gd php56w-mysql php56w-bcmath php56w-mbstring php56w-xml php56w-ldap

修改php配置
    vim /etc/php.ini 
    post_max_size = 16M
    max_execution_time = 300
    max_input_time = 300
    date.timezone = Asia/Shanghai
    always_populate_raw_post_data = -1

修改apache配置
    vim /etc/httpd/conf/httpd.conf
    ServerName 127.0.0.1
    DirectoryIndex index.html index.html.var index.php


启动httpd服务
    /etc/init.d/httpd start

测试php
    vi /var/www/html/index.php         #修改测试页内容，测试zabbix用户是否能够登陆数据库，这个环节很重要
    <?php
    $link=mysql_connect('10.0.99.35','zabbix','zabbix'); 
    if($link) echo "<h1>Success!!</h1>";   #显示Success表示连接数据库成功
                                                                                                        else echo "Fail!!";
    mysql_close();
    ?>

    curl http://127.0.0.1/index.php
    
依赖包安装
    yum -y install gcc mysql-community-devel libxml2-devel unixODBC-devel net-snmp-devel libcurl-devel libssh2-devel OpenIPMI-devel openssl-devel openldap-devel

mysql sql导入（上面是源码包里的，下面是yum安装的目录下才有的。本质上都是一样的东西）
    [1. 下载zabbix，导入sql
    tar -zxvf zabbix-4.0.1.tar.gz
    cd zabbix-4.0.1/database/mysql/
    ls ->
    	data.sql images.sql schema.sql
    mysql -uzabbix -p zabbix < schema.sql 
    mysql -uzabbix -p zabbix < images.sql 
    mysql -uzabbix -p zabbix < data.sql 
    2. zcat /usr/share/doc/zabbix-server-mysql-版本号/create.sql.gz | mysql -uzabbix -p -h 127.0.0.1 zabbix   #导入数据到数据库zabbix中(最后一个zabbix是数据库zabbix)，且因为用户zabbix是%(任意主机)，所以登录时需要加上当前主机ip(-h 127.0.0.1),密码是用户zabbix登陆密码zabbix
    ]


安装zabbix-server（两种方案2选1吧，我是用的第二种，但是第一种编译运行不确定可行）
[1. 		
    cd /zabbix-4.0.1
    编译
    ./configure --enable-server --enable-agent --with-mysql --enable-ipv6 --with-net-snmp --with-libcurl --with-libxml2 --with-unixodbc --with-ssh2 --with-openipmi --with-openssl --prefix=/usr/local/zabbix
    安装
    [root@localhost zabbix-4.0.1]# make install
    [root@localhost zabbix-4.0.1]# echo $?
    12 、修改zabbix_server的配置

    vi /usr/local/zabbix/etc/zabbix_server.conf
    DBName=zabbix
    DBUser=zabbix
    DBPassword=zabbix
2. 
    yum install zabbix-server-mysql zabbix-web-mysql -y    #安装zabbix组件
    zcat /usr/share/doc/zabbix-server-mysql-版本号/create.sql.gz | mysql -uzabbix -p -h 127.0.0.1 zabbix
    ]

主要是yum安装server可能会出现没有web界面的情况（一切日志正常，但是没有界面），就需要从源码包内提取web界面的内容
    mkdir /var/www/html/zabbix
    cd /zabbix-4.0.1/frontends/php/
    cp -rf  *  /var/www/html/zabbix/
	chown -R apache:apache /var/www/html/zabbix #设置Apache作为Web用户接口文件的所有者
	chmod +x /var/www/html/zabbix/conf/ #添加权限给Zabbix Web界面执行文件

添加Zabbix服务器和Zabbix代理启动脚本
	cp /zabbix-4.0.1/misc/init.d/fedora/core/zabbix_server /etc/init.d/zabbix_server
	cp /zabbix-4.0.1/misc/init.d/fedora/core/zabbix_agentd /etc/init.d/zabbix_agentd

添加Zabbix服务器和Zabbix代理服务
    chkconfig --add /etc/init.d/zabbix_server
    chkconfig --add /etc/init.d/zabbix_agentd
    chkconfig httpd on
    chkconfig mysqld on
    chkconfig zabbix_server on
    chkconfig zabbix_agentd on
    
    
    
zabbix-java-gateway的编译安装
	./configure  --prefix=/etc/zabbix/zabbix_java_gateway --enable-java
	make
	make install
	
	yum install -y gcc texinfo-tex flex zip libgcc.i386 glibc-devel.i386  #遇到编译需要gcc的情况

	以上的下载源码包编译安装的情况，事实上我觉得可以直接yum install（没有测试）
	rpm -ivh http://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm 
    或 rpm -ivh http://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-java-gateway-4.0.1-1.el7.x86_64.rpm
	yum install zabbix-java-gateway
    
    vi /etc/zabbix/zabbix_server.conf  #修改zabbix_server.conf
    JavaGateway=127.0.0.1
    JavaGatewayPort=10052
    StartJavaPollers=4

    vi /etc/zabbix/zabbix_java_gateway/sbin/zabbix_java/settings.sh  #修改zabbix_java_gateway配置
    LISTEN_IP="0.0.0.0"
    LISTEN_PORT=10052
    START_POLLERS=5

	./zabbix_java_gateway/sbin/zabbix_java/startup.sh  #启动zabbix_java_gateway
	
	service zabbix-server restart  #重启zabbix-server