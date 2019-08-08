
### 服务开启与关闭
```
    开启
    service mysql start

    关闭
    service mysql stop

    重启
    service mysql restart
```

### 登录
```
    密码明文
    语法：mysql -u用户名 -p用户密码
    eg：mysql -uroot -p123456

    密码密文
    语法：mysql -u用户名 -p+回车，然后输入密码
    eg：mysql -uroot -p　　
```
　　
### 查看数据库结构
```
    显示数据库列表
    show databases;

    显示库中的数据表
    use mysql;
    show tables;

    显示数据表结构
    describe 数据表名;
```
[资料来源](https://www.cnblogs.com/MIC2016/p/8287897.html)
