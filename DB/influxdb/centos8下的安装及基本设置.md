1. 安装
vi  /etc/yum.repos.d/influxdb.repo
    [influxdb]
    name = InfluxDB Repository
    baseurl = https://repos.influxdata.com/rhel/7/x86_64/stable/
    enabled = 1
    gpgcheck = 1
    gpgkey = https://repos.influxdata.com/influxdb.key
yum makecache
yum -y install influxdb
sudo systemctl enable --now influxdb


2. 登录
influx #无用户验证时进入命令行
show databases #显示所有数据库
create database "xxx" 创建数据库
use xxx #使用数据库
show measurements #显示该库中所有表

3. 创建用户
create user "root" with password 'newpwd' with all privileges
show users #可以看见admin=true，不加'with all privileges'则为false
drop user root #删除用户

4. 配置认证策略
vi /etc/influxdb/influxdb.conf 
    auth-enabled=true
systemctl restart influxdb    

5. 安装chronograf
wget https://dl.influxdata.com/chronograf/releases/chronograf-1.8.10.x86_64.rpm #安装与influxdb同版本的
yum localinstall chronograf-1.8.10.x86_64.rpm 
systemctl start chronograf
systemctl enable chronograf
打开网页登录吧：http://xxx.xxx.xxx.xxx:8888 ，疑似需要对外开放8086端口，不然登录验证不通过