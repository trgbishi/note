前提，9号机上oracle已经搭建好，jdbc可用，存在用户名密码可用
28号机zabbix server已经安装好


##下载orabbix
https://sourceforge.net/projects/orabbix/files/orabbix-1.2.3.zip/download

mkdir /opt/orabbix
mv orabbix-1.2.3.zip  /opt/orabbix
unzip orabbix-1.2.3.zip

##复制启动脚本
cp /opt/orabbix/init.d/orabbix /etc/init.d/orabbix

##赋权
chmod +x /etc/init.d/orabbix
chmod +x /opt/orabbix/run.sh
chkconfig --add orabbix

##核心配置文件config.props
cd /opt/orabbix/conf
cp config.props.sample config.props

##需要配置的参数
###ZabbixServerList=ZabbixServer1,ZabbixServer2,ZabbixServer3
ZabbixServerList=ZabbixServer#可扩展
ZabbixServer1.Address=*.*.*.28 #zabbix服务器ip
ZabbixServer1.Port=10051 ##zabbix服务器端口

###DatabaseList=DB1,DB2,DB3 ##数据库列表，名称随便起,这个真的是随便起，不必和数据库名字对应上
DB1.Url=jdbc:oracle:thin:@*.*.*.9:1521:test ##数据库连接串
DB1.User=****** ##监控数据库用户名
DB1.Password=****** ##监控数据库口令

下载的orabbix-1.2.3.zip里有模板，可以导入Orabbix_export_full.xml，这个网上教程都说是最全的。
新建主机，主机名称填刚才的DB1
代理接口填的*.*.*.9，端口1521
会报错，但是oracle的监控数据过一会就能查到了。
这里报错应该是oracle所在机器上并没有zabbix agent对应的缘故吧


