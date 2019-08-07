## 服务端（被控制端）

1. 安装vncserver
	sudo apt-get install tightvncserver

    > 首次启用vncserver会提示初始化密码
    >如果没有，或者之后需要重置
    ```
        vncpasswd
    ```

2. 打开.vnc/xstartup，并且直接覆盖(以下能同时解决客户端灰屏问题)
```
	#!/bin/sh
    export XKL_XMODMAP_DISABLE=1	 
    unset SESSION_MANAGER	
    unset DBUS_SESSION_BUS_ADDRESS
    gnome-panel &	
    gnmoe-settings-daemon &	
    metacity &	
    nautilus &	
    gnome-terminal &
```

3. 控制模式选择(only view || ...)
```
    only-view mode:
    	gsettings set org.gnome.Vino network-interface lo 
    another mode:
    	gsettings reset org.gnome.Vino network-interface 
```

4. 启动服务  
```    
    vncserver :1  
```

5. 关闭服务
```
	vncserver -kill :1  
```


## 客户端（控制端）
1. windows系统  
```
    安装VNC Viewer
```

2. ubuntu系统
```
	sudo apt-get install xvnc4viewer  
	vncviewer 服务端IP:1  #启动并连接服务端的窗口
```


>可选：
    sudo apt-get install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal  