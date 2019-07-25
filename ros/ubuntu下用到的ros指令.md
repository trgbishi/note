自动补全需要的lib库
$ rosdep install --from-paths ~/catkin_ws/src --ignore-src
 
打印话题
$ rostopic echo /scan
 
录制数据包
$ rosbag record /scan -O tmp
 
回放数据包
$ rosbag play tmp.bag
 
publisher topic
rostopic pub /heartbeat cotek_msgs/HeartBeat "{nodeId: 1, speed: 2, status: 3, battery: 4, odom: 5, sequence: 6}" 
 
查看分支
git branch
 
切换分支到***
git checkout -b ***
 
上传代码到git远程
git status
git add -A
git commit -m "&*(&*"
git push
 
rosrun格式
rosrun package-name executable-name

给usb设备赋权限
sudo chmod 666 /dev/ttyUSB0