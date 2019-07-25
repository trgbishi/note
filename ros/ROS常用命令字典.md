版权声明：本文为转载原创文章，转载请标明原出处: http://www.cnblogs.com/liu-fa/p/5761448.html

该博文适合已经具备一定的ROS编程基础的人，快速查看ROS相关指令。

创建 ROS 工作空间

启动 ROS

$ roscore
创建工作环境

$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace
编译 ROS 程序

$ cd ~/catkin_ws
$ catkin_make
添加程序包到全局路径

$ echo "source catkin_ws/devel/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
Package 相关操作

创建 Package 并编译

$ cd ~/catkin_ws/src
$ catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
$ cd ~/catkin_ws
$ catkin_make
查找 Package

$ rospack find [package name]
查看 Package 依赖

$ rospack depends <package_name>
$ rospack depends1 <package_name>
Node 相关操作

查看所有正在运行的 Node

$ rosnode list
查看某节点信息

$ rosnode info [node_name]
运行 Node

$ rosrun [package_name] [node_name] [__name:=new_name]
Topic 相关操作

查看 rostopic 所有操作

$ rostopic -h
查看所有 Topic 列表

$ rostopic list
图形化显示 topic

$ rosrun rqt_graph rqt_graph
$ rosrun rqt_plot rqt_plot
查看某个 Topic 信息

$ rostopic echo [topic]
查看 Topic 消息格式

$ rostopic type [topic]
$ rosmsg show [msg_type]
向topic发布消息

$ rostopic pub [-1] <topic> <msg_type> [-r 1] -- [args] [args]
Service 相关操作

查看所以service操作

$ rosservice -h
查看 service 列表

$ rosservice list
调用 service

$ rosservice call [service] [args]
查看 service 格式并显示数据

$ rosservice type [service] | rossrv show
设置service parameter

$ rosparam set [parame_name] [args] + rosservice call clear
获得parameter

$ rosparam get [parame_name]
加载parameter

$ rosparam load [file_name] [namespace]
删除parameter

$ rosparam delete
Bag 相关操作

录制所有topic变化

$ rosbag record -a
记录某些topic

$ rosbag record -O subset <topic1> <topic2>
查看bag信息

$ rosbag info <bagfile_name>
回放

$ rosbag play (-r 2) <bagfile_name>
