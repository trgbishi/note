    .1.3.6.1.2.1.25.2.3.1.4 | 簇的大小 | hrStorageAllocationUnits
    .1.3.6.1.2.1.25.2.3.1.5 | 簇的的数目 | hrStorageSize

    磁盘大小体现为hrStorageAllocationUnits * hrStorageSize
    而hrStorageSize在int32下，最大为2^31（正负各一半），为2^31=2*1024*1024*1024
    hrStorageAllocationUnits 为8192，即8kb簇
    总16TB

    修改/etc/snmp/snmpd.conf
    增加一行
    realStorageUnits 0
    即对hrStorageAllocationUnits进行扩容，从而保持hrStorageSize的32位最大大小

[linux参考](https://blog.csdn.net/redleaf0000/article/details/38303299?locationNum=14)