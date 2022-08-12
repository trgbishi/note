举个例子
sudo dpkg -i aaa.deb
报依赖缺少，执行以下自动补全依赖，再继续dpkg -i
sudo apt-get -f -y install
所有下载的文件都会出现在/var/cache/apt/archives目录


仅下载模式，可以将language-pack-zh-hans及其所需要的依赖，下载到/var/cache/apt/archives目录
aptitude --download-only install  language-pack-zh-hans -y



如果已经准备好了所有的离线包，现在面对一个干净的全新的系统，想要在离线环境下安装
首先将所有的离线deb文件上传到/var/cache/apt/archives
sudo dpkg -i aaa.deb 
如果报错依赖缺少,执行以下指令会优先在/var/cache/apt/archives内找上一条安装指令缺少的依赖包并安装上
sudo apt-get -f -y install