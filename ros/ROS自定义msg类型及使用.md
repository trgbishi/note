转自：http://blog.csdn.net/u013453604/article/details/72903398

首先创建一个空的package单独存放msg类型（当然也可以在任意的package中自定义msg类型）
这里为便于说明，建立一个名为test_msgs的包，用于对自定义msg类型的用法举例

$ cd catkin_ws/src
$ catkin_create_pkg test_msgs

1.新建msg文件

然后在test_msgs中创建msg文件夹，在msg文件夹其中新建一个名为Test.msg消息类型文件

$ cd test_msgs
$ mkdir msg

Test.msg的内容如下，
基本类型可参考: std_msgs、common_msgs

float32[] data
float32 vel
geometry_msgs/Pose pose
string name


2.修改package.xml

接下来需要message_generation生成C++或Python能使用的代码，需要message_runtime提供运行时的支持，所以package.xml中添加以下两句

<build_depend>message_generation</build_depend>
<run_depend>message_runtime</run_depend>
    
3.修改CMakeLists.txt

CMakeLists.txt要注意四个地方

(1)首先调用find_package查找依赖的包，必备的有roscpp rospy message_generation，其他根据具体类型添加，比如上面的msg文件中用到了geometry_msgs/Pose pose类型，那么必须查找geometry_msgs

find_package(catkin REQUIRED COMPONENTS roscpp rospy message_generation std_msgs geometry_msgs)

(2)然后是add_message_files，指定msg文件

add_message_files(
  FILES
  Test.msg
  # Message2.msg
)

(3)然后是generate_messages，指定生成消息文件时的依赖项，比如上面嵌套了其他消息类型geometry_msgs，那么必须注明

#generate_messages必须在catkin_package前面
generate_messages(
 DEPENDENCIES
 geometry_msgs
)


(4)然后是catkin_package设置运行依赖

catkin_package(

CATKIN_DEPENDS message_runtime

)

到这里新的msg类型test_msgs/Test就可以使用了，下面编译这个包，然后利用rosmsg show指令查看

$ cd catkin_ws
$ catkin_make
$ rosmsg show test_msgs/Test 
float32[] data
float32 vel
geometry_msgs/Pose pose
  geometry_msgs/Point position
    float64 x
    float64 y
    float64 z
  geometry_msgs/Quaternion orientation
    float64 x
    float64 y
    float64 z
    float64 w
string name


二、msg的使用

要使用自定义的消息类型必须source自定义消息所在的工作空间，否则rosmsg show test_msgs/Test和rostopic echo /test_msg(/test_msg是节点中使用自定义消息类型test_msgs/Test的topic)都会报错，因为没有source的情况下自定义消息类型是不可见的，被认为是未定义类型
1.其他包调用自定义msg类型

参考：
DefiningCustomMessages
如果是在test_msgs包内的节点中调用test_msgs/Test类型，只需要在.cpp文件中如下调用即可

#include <test_msgs/Test.h>

test_msgs::Test msg;

如果是在其他包调用test_msgs/Test类型则需要修改package.xml和CMakeLists.txt，比如同样在工作空间catkin_ws内有一个名为test的包，我们可以在这个包内写一个节点，使用我们刚才自定义的消息类型test_msgs/Test，如下：

(1)修改package.xml
养成好习惯，维护软件包清单的更新，以便于别人使用你的软件前安装各种依赖项，当然这个文件不影响程序编译

<build_depend>roscpp</build_depend>
<run_depend>roscpp</run_depend>

<build_depend>test_msgs</build_depend>
<run_depend>test_msgs</run_depend>


(2)修改CMakeLists.txt
调用自定义消息类型主要修改两个地方，以下是重点：
一是find_package中需要声明查找包含该消息类型的包；
二是add_dependencies要注明该消息的依赖，其他地方和普通节点一样

find_package(catkin REQUIRED COMPONENTS
  roscpp
  geometry_msgs
  test_msgs
)

add_dependencies(test1 test_msgs_gencpp)#调用同一工作空间的自定义消息类型时注明依赖关系，防止发生头文件找不到的报错


如果缺少add_dependencies中对test_msgs_gencpp的依赖声明，在编译的时候如果先编译test包再编译test_msgs包则会出现如下报错（ROS工作空间各个软件包的编译顺序是随机的），因为头文件test_msgs/Test.h还未生成

fatal error: test_msgs/Test.h: 没有那个文件或目录
 #include "test_msgs/Test.h"


2.msg类型数组的使用

需要说明的是std_msgs中有些数组用法和C++标准库中不一样
比如Float32MultiArray，其定义如下：

std_msgs/MultiArrayLayout layout
float32[] data


其中data是一个浮点数组，但是方括号只是一个用来表明它是数组的符号，我们不能在定义的时候在方括号中给定数组长度，实际上ROS中类似float32[]，int8[]这样的数组类型都是std::vector，使用方法也和std::vector一样

测试代码可以从这里下载
下面是一个消息订阅节点，用于测试

/************************  
 * @Author: Jinglin Zhang  
 * @DateTime: 2017-06-07 19:57:30  
 * @Description: 节点test1,订阅了test_msgs包下talker节点发布的"test_msg"话题，用于测试test_msgs::Test消息类型  
************************/
#include <ros/ros.h>
#include <test_msgs/Test.h>

void msgCallback(const test_msgs::Test::ConstPtr &msg)
{
  //test_msgs::Test类型里的float32[]数据传到vector
  std::vector<float> array = msg->data;

  std::cout << "msg->data[0]=" << msg->data[0] << std::endl;
  std::cout << "msg->data.size=" << msg->data.size() << std::endl;
  std::cout << "msg->data=" << msg->data[0] << ", " << msg->data[1] <<  ", " << msg->data[2] << ", " <<  msg->data[3] << ", " <<  msg->data[4] << ", " <<  msg->data[5] << std::endl;

}

int main(int argc,char ** argv)
{
  ros::init(argc,argv,"test1");
  ros::NodeHandle n;

  ros::Subscriber msg_sub = n.subscribe("test_msg", 100, msgCallback);

  ros::spin();
  return 0;
}

下面是一个消息发布节点，用于测试

/************************  
 * @Author: Jinglin Zhang  
 * @DateTime: 2017-06-07 20:03:35  
 * @Description: 节点talker，发布"test_msg"话题，用于测试test_msgs::Test消息类型  
************************/ 
#include <ros/ros.h>
#include <test_msgs/Test.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "msg_talker");
  ros::NodeHandle n;
  ros::Publisher msg_pub = n.advertise<test_msgs::Test>("test_msg", 1000);
  ros::Rate loop_rate(10);
  int count = 0;

  while (ros::ok())
  {
    test_msgs::Test msg;
    std::cout << "msg.data.size=" << msg.data.size() << std::endl;

    //用vector给float32[]数组赋值
    float array[3] = {1.1,1.2,0.3};
    std::vector<float> array1(array,array+3);
    msg.data = array1;
    std::cout << "msg.data3[0]=" << msg.data[0] << std::endl;
    std::cout << "msg.data3.size=" << msg.data.size() << std::endl;

    //下标访问float32[]数组
    msg.data[0] = 0.1;
    std::cout << "msg.data3[0]=" << msg.data[0] << std::endl;


    float array4[4] = {1.0,2.0,0.3,6.6};
    std::vector<float> array41(array4,array4+4);
    msg.data = array41;
    std::cout << "msg.data4.size=" << msg.data.size() << std::endl;
    std::cout << "msg.data4=" << msg.data[0] << " " << msg.data[1] <<  " " << msg.data[2] << " " <<  msg.data[3] << std::endl;

    msg.data.push_back(5.5);
    std::cout << "msg.data[5]=" << msg.data[4] << std::endl;

    //使用迭代器
    msg.data.resize(6);
    std::cout << "msg.data6.size=" << msg.data.size() << std::endl;
    std::cout << "msg.data6=" ;
    for(std::vector<float>::iterator it = msg.data.begin(); it != msg.data.end(); ++it)
    {
      *it = 0.6;
      std::cout << *it << " ";
    }
    std::cout << std::endl;

    msg_pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }

  return 0;
}


trg附加
 package.xml文件中有两种格式，对应的书写模式不一样：
<run_depend>在模式1中的格式为：
<run_depend>foo</run_depend>
在模式2中的书写格式为：
<build_export_depend>foo</build_export_depend>
<exec_depend>foo</exec_depend>
你的xml文档应该用的是格式2，而你输入的格式1，所以会出错。改成格式2的书写方式就行了。
详细链接参照：
http://docs.ros.org/indigo/api/catkin/html/howto/format2/migrating_from_format_1.html
