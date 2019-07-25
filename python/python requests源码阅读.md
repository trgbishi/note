1.从当前目录下导入utils.py文件
	from . import test
2.从当前目录下的sessions.py导入session函数与Session类（此处导入的函数与类是并列的，该函数不属于任何类）
	from .sessions import session, Session
3.从当前目录下的status_codes.py中导入 codes字典（到这里可以发现，导入列表与元组都是一样的逻辑）
	from .status_codes import codes
4.导入模块还能进行异常捕获
    import logging
    try:  # Python 2.7+
        from logging import NullHandler
    except ImportError:
        class NullHandler(logging.Handler):
            def emit(self, record):
                pass
5.assert，如
    assert major == 3
    assert minor < 1
    assert patch >= 2
    
6.了解一下yml文件
如https://www.cnblogs.com/ListenWind/p/4518198.html
输出是字典格式
7.coveragerc文件
用于计算测试用例覆盖率，先了解这个东西的存在
8.rst文件
这个应该是阅读的文档，比如说明作者信息
9.markdown里-的用法
在行首加小圈圈
10.LICENSE
本项目遵循的授权许可
11.makefile
python也有makefile??
12.MANIFEST.in
此文件在打包的时候告诉setuptools还需要额外打包那些文件
13.pipenv 包管理工具
Pipfile 包含关于项目的依赖包的信息，并取代通常在Python项目中使用的requirements.txt文件
pipfile.lock 可以通过更新Pipfile.lock来冻结软件包名称及其版本，以及其依赖关系的列表
14.setup
setup.py是启动脚本
setup.cfg是配置文件
15.tox.ini
测试工具
