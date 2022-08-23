举个例子
sudo dpkg -i aaa.deb
报依赖缺少，执行以下自动补全依赖，再继续dpkg -i
sudo apt-get -f -y install
所有下载的文件都会出现在/var/cache/apt/archives目录


仅下载模式，可以将language-pack-zh-hans及其所需要的依赖，下载到/var/cache/apt/archives目录
aptitude --download-only install  language-pack-zh-hans -y


离线包制作
sudo mkdir -p /offlinePackage/repo
sudo cp -r /var/cache/apt/archives  /offlinePackage/repo
sudo chmod 777 -R /offlinePackage/
sudo apt-get install dpkg-dev
sudo dpkg-scanpackages /offlinePackage/ /dev/null |gzip >/offlinePackage/Packages.gz


离线包使用
sudo mkdir /offlinePackage
将repo文件夹与Packages.gz上传到offlinePackage目录下
sudo mv /etc/apt/sources.list /etc/apt/sources.list.back
sudo vi /etc/apt/sources.list
    deb [trusted=yes] file:/// offlinePackage/
sudo apt-get update