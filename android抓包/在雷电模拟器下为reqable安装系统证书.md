在雷电模拟器下为reqable安装系统证书

## 1.安装雷电模拟器
    官网下载，安装，略（https://www.ldmnq.com/）
## 2.安装PC端的reqable
    官网下载，安装，略（https://reqable.com/zh-CN/）
## 3.下载并安装证书
### 配置雷电模拟器权限
    设置里ROOT权限[开启]，并勾选[System.vmdk可写入]
### 下载
    启动pc端reqable，点击小盾牌，在弹出的页面左下角点下载，得到crt证书reqable-ca.crt
### 写入证书到系统证书路径
    将reqable-ca.crt拷贝到雷电模拟器根目录(有adb.exe)，如D:\leidian\LDPlayer9
    启动powershell，分别执行:
    .\adb root
    .\adb remount
    .\adb push reqable-ca.crt /system/etc/security/cacerts/364618e0.0
### 检查是否安装成功
    设置->安全性与位置信息->加密与凭据->信任的凭据：系统凭据中查找[Reqable,LLC]
## 4.配置wlan
    手动代理，填写ip与端口（默认是9000）


另，我本想再测一下fiddler证书拷贝到模拟器上试试，但可能是因为fiddler证书是cer格式或者其他原因，导致按照以上方案拷贝后没有显示安装成功，遂作罢。后续如有需求，可以考虑使用openssl将cer文件转化为crt或者其他格式再试试。不过reqable目前已经可以覆盖fiddler的功能，后续大概没有给fiddler安装系统证书的必要了<br>

另，reqable的crt证书直接作为用户证书安装到我的手机上失败，而fiddler的cer证书却可以作为用户证书安装到我手机上。