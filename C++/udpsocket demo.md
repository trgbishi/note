//编译
>> g++ client.cpp -o client
>> g++ server.cpp -o server
//运行
>> ./server
>> ./client



client.cpp
#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>//for "close()"
#include <arpa/inet.h>//for "inet_addr"


#define SERVER_PORT 8888
#define BUFF_LEN 512
#define SERVER_IP "192.168.0.40"


void udp_msg_sender(int fd, struct sockaddr* dst)
{

    socklen_t len;
    struct sockaddr_in src;
    while(1)
    {
        char buff[BUFF_LEN] = "test";
        len = sizeof(*dst);
        std::cout<<"client:"<<buff<<std::endl;  //打印自己发送的信息
        sendto(fd, buff, BUFF_LEN, 0, dst, len);
        memset(buff, 0, BUFF_LEN);
        recvfrom(fd, buff, BUFF_LEN, 0, (struct sockaddr*)&src, &len);  //接收来自server的信息

        std::cout<<"server:"<<buff<<std::endl;
        sleep(1);  //一秒发送一次消息
    }
}

/*
    client:
            socket-->sendto-->revcfrom-->close
*/

int main(int argc, char* argv[])
{
    int client_fd;
    struct sockaddr_in ser_addr;

    client_fd = socket(AF_INET, SOCK_DGRAM, 0);
    if(client_fd < 0)
    {
        std::cout<<"create socket fail!"<<std::endl;
        return -1;
    }

    memset(&ser_addr, 0, sizeof(ser_addr));
    ser_addr.sin_family = AF_INET;
    ser_addr.sin_addr.s_addr = inet_addr(SERVER_IP);
    //ser_addr.sin_addr.s_addr = htonl(INADDR_ANY);  //注意网络序转换
    ser_addr.sin_port = htons(SERVER_PORT);  //注意网络序转换

    udp_msg_sender(client_fd, (struct sockaddr*)&ser_addr);

    close(client_fd);

    return 0;
}

server.cpp
//#include <stdio.h>
#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>

#define SERVER_PORT 8888
#define BUFF_LEN 1024

void handle_udp_msg(int fd)
{
    char buff[BUFF_LEN];  //接收缓冲区，1024字节
    socklen_t len;
    int count;
    struct sockaddr_in clent_addr;  //clent_addr用于记录发送方的地址信息
    while(1)
    {
        memset(buff, 0, BUFF_LEN);
        len = sizeof(clent_addr);
        count = recvfrom(fd, buff, BUFF_LEN, 0, (struct sockaddr*)&clent_addr, &len);  //recvfrom是拥塞函数，没有数据就一直拥塞
        if(count == -1)
        {
            std::cout<<"recieve data fail!\n"<<std::endl;
            return;
        }
        std::cout<<"I have recieved " << count << " bytes data!"<<std::endl;  //回复client

        std::cout<<"client"<<buff<<std::endl;  //打印client发过来的信息
        memset(buff, 0, BUFF_LEN);

        std::cout<<"server:"<<buff<<std::endl;  //打印自己发送的信息给

        sendto(fd, buff, BUFF_LEN, 0, (struct sockaddr*)&clent_addr, len);  //发送信息给client，注意使用了clent_addr结构体指针
	std::cout<<"sendto success"<<std::endl;



    }
}


/*
    server:
            socket-->bind-->recvfrom-->sendto-->close
*/

int main(int argc, char* argv[])
{
    int server_fd, ret;
    struct sockaddr_in ser_addr; 

    server_fd = socket(AF_INET, SOCK_DGRAM, 0); //AF_INET:IPV4;SOCK_DGRAM:UDP
    if(server_fd < 0)
    {
        std::cout<<"create socket fail!"<<std::endl;
        return -1;
    }

    memset(&ser_addr, 0, sizeof(ser_addr));
    ser_addr.sin_family = AF_INET;
    ser_addr.sin_addr.s_addr = htonl(INADDR_ANY); //IP地址，需要进行网络序转换，INADDR_ANY：本地地址
    ser_addr.sin_port = htons(SERVER_PORT);  //端口号，需要网络序转换

    ret = bind(server_fd, (struct sockaddr*)&ser_addr, sizeof(ser_addr));
    if(ret < 0)
    {
        std::cout<<"socket bind fail!"<<std::cout;
        return -1;
    }

    handle_udp_msg(server_fd);   //处理接收到的数据

    close(server_fd);
    return 0;
}