参考 https://blog.csdn.net/zhengholien/article/details/77184486

1.创建war包
    Build -> Build Artifacts
2.创建tomcat server
    右上角 Edit Configurations -> Tomcat Server -> 具体项目 -> Server -> Application server | Open browser 端口号修改 | JRE 配置 | Tomcat Server Settings 修改 HTTP port
3.部署war包到tomcat上
    右上角 Edit Configurations -> Tomcat Server -> 具体项目 -> Deployment -> add -> Artifact

ps:原文需要把maven依赖添加到lib下，这一项我没有用到。可能是新IDE和新建的项目才需要配？
