zabbix server 无法启动时可能会报无法连接数据库，原因是too many connections
主要原因是zabbix需要的连接数，数据库max_connections无法提供
为何无法提供呢，zabbix server用一个还不够吗
不够的，zabbix_server.conf里每个poller都需要一个连接，这一点可以在zabbix启动后，在mysql客户端内查询：show full processlist，来自于zabbix的进程和pollers数量一致，可能是sleep状态，但是必须有

所以解决问题的方案有两种：
1. 修改mysql最大连接数
    临时修改
        set global max_connections=xxxx;
    永久修改
        找到my.cnf，依次检查弹出来的路径，看看是哪一个
            mysqld --verbose --help |grep -A 1 'Default options'
        修改max_connections=xxxx
        若没有，则在[mysqld]标签下添加
2. 修改zabbix pollers数量
    在zabbix_server.conf里修改