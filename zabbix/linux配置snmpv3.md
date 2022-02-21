### 先关闭snmpd
service snmpd stop

### 配置v3凭证
按要求依次输入用户名、authpass、encrypass。此处默认MD5和DES
net-snmp-config --create-snmpv3-user  -ro
    $ testtttt
    $ authpass00
    $ encrpass00


### 重启snmpd
service snmpd start

### 测试
snmpwalk -v3 -u testtttt -l authpriv -a MD5 -A authpass00 -x DES -X encrpass00 127.0.0.1 1
