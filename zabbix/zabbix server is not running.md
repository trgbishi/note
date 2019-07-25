1.通过直接跑server 配置文件来看报错
	/usr/sbin/zabbix_server -c /etc/zabbix/zabbix_server.conf
2.很可能是server初始内存不够用引起的
	cat /var/log/zabbix/zabbix_server.log | out of
  看看有没有out of memory的错误
  如果有，修改	/etc/zabbix/zabbix_server.conf 里的CacheSize参数 到1024M