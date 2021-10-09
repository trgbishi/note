### 上传离线yum包至/data/yum 路径下

### 创建本地仓库
```
    #yum install createrepo
    createrepo /data/yum
```
### 编辑yum的repo文件,指向创建的本地仓库
```
    cd /etc
    mv yum.repos.d yum.repos.d.bak
    mkdir yum.repos.d
    cd yum.repos.d
    
    建议手动输入，粘贴会出错：Bad id for repo
    vi Centos-Local.repo
    [Centos­Local] 
    name=centos yum repo 
    baseurl=file:///data/yum 
    enabled=1 
    gpgcheck=0 
    priority=1
```

### 清理yum缓存
```
    yum clean all
```

### 列出可安装的软件列表
```
    yum list
```