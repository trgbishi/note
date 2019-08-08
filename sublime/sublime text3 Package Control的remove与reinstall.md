来自两篇文章。

[卸载方法](http://blog.csdn.net/xiaowei_jin/article/details/51319269)
1. Preferences > Settings – User   /    首选项>设置-用户   ，打开后，ignored_packages中有Package Control，则去掉；
2. Preferences > Browse Packages…，打开后删除package control文件夹，返回上一级文件夹，进入Installed Packages，删除Package Control.sublime-package

[Package Control 安装方法](http://www.cnblogs.com/waising/articles/3466120.html)
1. 通过快捷键 ctrl+` 或者 View > Show Console 打开控制台，然后粘贴相应的 Python 安装代码；
2. Sublime Text 3 安装代码并回车：
```
import urllib.request,os; 
pf = 'Package Control.sublime-package'; 
ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( 		urllib.request.ProxyHandler()) );
open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
```
3. 重启Sublime Text 3；
4. 如果在Perferences->package settings中看到package control这一项，则安装成功。

