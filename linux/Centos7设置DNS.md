### 查看确认
cat /etc/resolv.conf

### 查看当前网络连接
nmcli connection show

### 配置当前网络连接对应的dns服务器
nmcli con mod eth0 ipv4.dns "114.114.114.114 8.8.8.8"

### 使配置生效
nmcli con up eth0

### 确认
查看cat /etc/resolv.conf确认更新，然后尝试ping www.baidu.com看是否完成解析