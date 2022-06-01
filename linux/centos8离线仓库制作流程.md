1. 离线包制作过程略，使用downloadonly，与centos7相同<br>
2. 创建目录<br>
    mkdir -p /root/my/repo<br>
    将离线包拷贝到/root/my/repo<br>
3. 安装createrepo<br>
    cd /root/my/repo<br>
    rpm -ivh createrepo_c-0.17.2-3.el8.x86_64.rpm  createrepo_c-libs-0.17.2-3.el8.x86_64.rpm <br>drpm-0.4.1-3.el8.x86_64.rpm <br>
4.  创建本地仓库<br>
    createrepo /root/my<br>
5. 备份yum源配置<br>
    mv /etc/yum.repos.d/ /etc/yum.repos.d.bak<br>
6. 创建本地yum源配置<br>
    mkdir /etc/yum.repos.d<br>
    vi /etc/yum.repos.d/local.repo<br>
        [local-repo]<br>
        name=local-repo<br>
        baseurl=file:///root/my/<br>
        enabled=1<br>
        gpgcheck=0<br>
7. 清空缓存并生成新的缓存<br>
    yum clean all<br>
    yum makecache<br>
8. 安装modulemd-tools<br>
    dnf install modulemd-tools<br>
9. 创建modular metadata<br>
    cd /root/my<br>
    repo2module  -s stable  .  modules.yaml<br>
    modifyrepo_c --mdtype=modules modules.yaml repodata/<br>
10. 重新生成缓存<br>
    yum makecache<br>

11. 备注<br>
    a. 测试镜像为：CentOS-8.4.2105-x86_64-dvd1<br>
    b. repo2module指令在查到的资料上是repo2module  -s stable  -d .  modules.yaml，但是下载到的<br>版本不适用该指令<br>
    c. 创建modular metadata主要是为了处理包含module相关的包<br>
    d. modulemd-tools的离线包也是通过downloadonly直接下载modulemd-tools-0.7-6.el8.noarch.rpm，<br>依赖包是：libmodulemd 2.13.0-1,python3-createrepo_c 0.17.2-3,python3-libmodulemd 2.13.0-1<br>