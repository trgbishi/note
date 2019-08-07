>已配置好Zabbix和Grafana

### 安装zabbix插件
    grafana-cli plugins install alexanderzobnin-zabbix-app
    systemctl restart grafana-server

### 启用zabbix插件
    在grafana界面启用

### 配置数据源
    URL：http://host/zabbix/api_jsonrpc.php 
    Username与Password填zabbixweb端登录密码
    另外，在zabbix dashboard最上方的Zabbix Data Source配置的是panel里metrics里的$datasource参数