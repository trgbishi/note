### 将语句添加到文件末尾，不用vi,不用gedit，直接添加！！
    echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
    source ~/.bashrc


### 设置环境变量的三种情况
* export 设置环境变量是临时的
* /etc/profile 是全用户永久
* ~/.bashrc 是对当前用户

>source指令是执行脚本，执行完只在当前shell有效。
而source ~/.bashrc ，~/.bashrc是每次登录以及打开新的shell时运行一次，所以在shell内修改完~/.bashrc后，新输入的指令并不能在当前终端使用，所以需要source一下。
所以对于那些不会自动运行的脚本，我们想要它执行的话，就要source一下。

### cd的使用
cd -返回上一次的工作路径
cd ../.. 连续两个..


## 文本处理
###grep,awk,sed是对文本处理的指令,具体用法用的时候再查


* history
可以查看历史指令，相比与上翻来得更加清晰


* head
可以直接看文件的开头，cat是直接从尾部开始，tail是只看尾部
当然，它们都是可以加参数的

* nohup
将脚本执行的输出日志重定向，如
nohup start.sh > task.log &

    >其中，start.sh是执行的脚本  task.log是日志目标文件，最后的 & 说明该重定向操作是后台运行的
    此外：
    1>  表示标准输出重定向
    2>  表示标准错误重定向
    因此2>&1 表示将标准错误重定向到标准输出
    nohup默认只有无参情况下只有标准输出，但使用 2>&1 即表示将stderr与stdout都重定向到如上的task.log中
    完整写法：nohup start.s > task.log 2>&1 &


* tail  
直接查看文件末尾
列举加参数的情况

* tail -f     
根据文件描述符进行追踪，当文件改名或被删除，追踪停止

* tail -F    
根据文件名进行追踪，并保持重试，即该文件被删除或改名后，如果再次创建相同的文件名，会继续追踪
    >ctrl+s，暂停刷新
    ctrl+q，继续刷新