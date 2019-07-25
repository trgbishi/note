原文来自http://www.cnblogs.com/liu-fa/p/5779206.html

添加源
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

设置密钥
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116

先换了科大的源（这里换什么都行吧，我不换不行）
sudo apt-get update

安装
sudo apt-get install ros-kinetic-desktop-full

查看可使用的包
apt-cache search ros-kinetic

初始化
sudo rosdep init
rosdep update

环境变量
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc

常用插件
udo apt-get install python-rosinstall

启动
roscore