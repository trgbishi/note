### 测试指令
    snmpwalk -v 3 -u username -l authPriv -a md5 -A authpass -x des -X privpass xxx.xxx.xxx.xxx ".1.3.6.1.2.1"
    snmpwalk -v 3 -u username -l authNoPriv -a sha -A authpass xxx.xxx.xxx.xxx ".1.3.6.1.2.1"
    snmpwalk -v 3 -u username -l noAuthNoPriv xxx.xxx.xxx.xxx ".1.3.6.1.2.1"
    ps:其中-a md5或sha,-x des或aes