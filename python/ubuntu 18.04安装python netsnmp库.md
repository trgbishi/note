### 说明
windows不支持python netsnmp的编译安装，主要是gcc以及一些其他的依赖
新系统会缺少很多小插件，或者插件版本不对，缺什么补什么。

### 准备
以下是我新系统需要装的
```
    sudo apt-get install python3-distutils
    sudo apt-get install -y python3-setuptools
    sudo apt install python3.6-dev
    sudo apt-get install libxml2-dev libxslt1-dev
    sudo apt-get install zlib1g-dev
    sudo apt-get install libevent-dev
```

下载[net-snmp-5.7.3.tar.gz](http://www.net-snmp.org/download.html)  
下载支持python3的[netsnmp版本](https://github.com/bluecmd/python3-netsnmp)

### 安装
安装net-snmp
```
    tar -zxvf net-snmp-5.7.3.tar.gz
    cd net-snmp-5.7.3
    ./configure --disable-embedded-perl --without-perl-modules #忽略perl..--with-python-modules可以直接把python模块，即netsnmp库安装好，但是这里的库不支持python3，甚至还有space与tab混用的报错
    make
    sudo make install
```

安装python3-netsnmp
```
    python setup.py build
    python setup.py test (requires a locally running agent w/ config provided)
    python setup.py install
```