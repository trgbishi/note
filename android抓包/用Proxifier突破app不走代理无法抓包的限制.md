## 需要的工具
    1. Proxifier
    2. 抓包工具，我用的reqable
## reqable配置
    官网下载安装包，安装后通过小盾牌给本地windows安装证书；
## Proxifier配置
    需要找一下安装包安装，参考资料中的安装包可用
    填写抓包工具的ip和端口，以及抓取的协议，reqable的端口是9000：
        Profile(菜单栏配置文件)->Proxy Servers(代理服务器)->Add:[127.0.0.1,9000,HTTPS]->OK
        弹出窗口是否作为默认服务器：Y
        弹出窗口提示发现回环要创建规则：勾选Apply，点击ok
## 启动reqable
    此时，启动reqable就会有数据了，可以在reqable过滤出想要的接口
    核心逻辑就是让Proxifier来代理并转发数据到抓包工具









参考资料：https://www.elecfans.com/d/2023354.html