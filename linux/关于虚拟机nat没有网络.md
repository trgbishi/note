1.VMware的编辑->虚拟网络编辑器建立NAT网络
2.windows服务里VMware DHCP Service、VMware NAT Service、VMware Workstation Server要启动
3.将1中建立的网络，在windows网络和共享中心中，自动获取ip地址，自动获取DNS服务器地址
4.查看/etc/sysconfig/network-scripts/ifcfg-xxx ,是否设置为 onboot = no ,修改为yes
5.重启