## IDEA打包
- 配置方式
    
    **File -> Project Structure -> Artifacts -> Add -> JAR -> From modules with dependencies -> 选择Module 、 Main Class  、Directory for META-INF/MANIFEST.MF(这个目录可能需要和Main Class一个目录)  -> OK -> OK**
- 打包方式

    **Build -> Build Artifacts -> 按需**

## java service wrapper
- 其实本质上和java -jar hello.jar一个逻辑，主要是实现了当成windows服务或- linux守护线程来使用
- bin目录是启动脚本存放位置，不需要每次都改
- conf目录是配置文件存放位置
- lib存在要执行的jar包（而不是用来存放执行项目依赖的jar），除了自带的wrapper.jar 建议只放一个当前执行的jar
- logs目录存在wrapper.log，即java service wrapper的log

### 配置文件说明：
- 要记得配置java所在路径，如果担心机器上没有，可以自己带java环境，用相对路径

    **wrapper.java.command=%JAVA_HOME%/bin/java**
- 是否启用wrapper 终端命令执行时的debug

    **wrapper.debug=FALSE**
- 是否启用wrapper自带的log，在logs目录下。NONE为不启用

    **wrapper.logfile.loglevel=DEBUG**

### 脚本执行方式
- bin/demoapp

