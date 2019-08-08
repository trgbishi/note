### 准备
>三台机器 CentOS Linux release 7.4.1708 (Core)
>10.0.99.40
>10.0.99.41
>10.0.99.42

### 一致性工作
#### 下载安装包
```
wget https://downloads.mongodb.com/linux/mongodb-linux-x86_64-enterprise-rhel70-3.4.19.tgz
```
#### 解压
```
tar -zxvf mongodb-linux-x86_64-enterprise-rhel70-3.4.19.tgz

mv mongodb-linux-x86_64-enterprise-rhel70-3.4.19 /root/software/mongo_primary  #40机器
mv mongodb-linux-x86_64-enterprise-rhel70-3.4.19 /root/software/mongo_secondry #41机器
mv mongodb-linux-x86_64-enterprise-rhel70-3.4.19 /root/software/mongo_arbiter #42机器
```

#### 环境变量
```
vi /etc/profile
    export PATH=$PATH:/root/software/mongo_primary #40机器
    export PATH=$PATH:/root/software/mongo_secondry #41机器
    export PATH=$PATH:/root/software/mongo_arbiter #42机器
```

#### 配置文件
```
vi mongodb.conf
    pidfilepath=/data/mongo/log/mongod.pid
    logpath=/data/mongo/log/mongod.log
    dbpath=/data/mongodb
    logappend=true
    bind_ip=10.0.99.40-42 #bind当前机器的ip
    port=27017
    fork=true
    replSet=rs0
```

#### primary
```
$ mongo 10.0.99.40:27017 --config /配置路径/mongodb.conf
$ mongo 10.0.99.40:27017
初始化复制集
 >rs.initiate({_id: "rs0",members: [{ _id: 0 , host: "10.0.99.40:27017" }]})

新增成员
 >rs.add("10.0.99.41:27017")
新增仲裁
 >rs.addArb("10.0.99.42:27017")
```

### 其它
1. 主从集群下，从节点同步主节点数据，从节点无法进行写操作。当主节点停掉后，当剩余从节点个数（或网络断开后，仍然保持互相通信的节点数）>总结点的一半时，选举出新的primary。像一主一从这种无法选举新主节点的情况，可以通过引入仲裁者。
2. 主-从-仲裁下，主节点停掉后，会有一个从节点变成主节点，当原主节点重连后，自动成为从节点
3. [资料来源1](https://www.cnblogs.com/kevingrace/p/7881496.html),[资料来源2](http://forum.foxera.com/mongodb/topic/561/mongodb%E6%95%85%E9%9A%9C%E5%88%87%E6%8D%A2%E6%9C%BA%E5%88%B6%E6%98%AF%E6%80%8E%E6%A0%B7%E7%9A%84/3)