本地
services.msc
启动两个服务：
OracleServiceORCL
oracleOraDb11g_home1TNSListener
 
 
连接sql
sqlplus / as sysdba
 
有问题再加
 
 
 
连接远程
 conn user/password@ip:port/itsm
 远程要是出了适配器啊，无监听程序的报错，而且没有登录系统的权限的话，就改不了。