服务端，即被控制端需要做的
================================================
安装vncserver
-------------------------------------------------
	sudo apt-get install tightvncserver

首次启用vncserver会提示初始化密码
如果没有，或者之后需要重置
-------------------------------------------------
	vncpasswd

打开.vnc/xstartup，并且直接覆盖(以下能同时解决客户端灰屏问题)
-------------------------------------------------
	#!/bin/sh
    export XKL_XMODMAP_DISABLE=1	 
    unset SESSION_MANAGER	
    unset DBUS_SESSION_BUS_ADDRESS
    gnome-panel &	
    gnmoe-settings-daemon &	
    metacity &	
    nautilus &	
    gnome-terminal &

控制模式选择(only view || ...)
-------------------------------------------------
only-view mode:
	gsettings set org.gnome.Vino network-interface lo 
another mode:
	gsettings reset org.gnome.Vino network-interface 

启动服务
-------------------------------------------------
	vncserver :1  

关闭服务
-------------------------------------------------
	vncserver -kill :1  


windows系统安装VNC Viewer
===================================================
ubuntu系统
===================================================

安装
---------------------------------------------------
	sudo apt-get install xvnc4viewer  

启动并连接服务端的窗口
---------------------------------------------------
	vncviewer 服务端IP:1  



可选：
    sudo apt-get install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal  