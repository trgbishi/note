这个是原来存在手机备忘的，也是尝试了网上很多办法后得到的结果。没有记方法来源。

1. 普通用户修改密码方法  
    重启Ubuntu，随即长按shift进入grub菜单； 
    选择recovery mode，回车确认,如下图； 

    在Recovery Menu中，选择“Root Drop to root shell prompt”，回车确认，如下图； 

    进入shell界面，使用passwd命令重新设定密码：passwd david，(david是系统中已有的username，但是如果root的用户就会有authentication token manipulation error错误，对于修改root用户的密码情况，可以参考下面的‘root用户修改密码方法’)，回车确认； 
    输入新密码； 
    再次确认新密码； 
    看到密码设定成功提示：passwd: password updated successfully； 
    重启系统进入GUI界面：sudo reboot； 

2. root用户修改密码方法   
    重启Ubuntu，随即长按shift进入grub菜单； 
    选择recovery mode，即Ubuntu，With Linux 3.2.0-23-generic（recovery mode），按e，编辑启动参数， 
    把ro recovery nomodeset 改成rw single init=/bin/bash

    然后按ctrl+x 或者F10   就可以进入 单用户模式， 
    此时可以修改root 密码，通过passwd root修改root 密码。

    重启Ubuntu，随即长按shift进入grub菜单； 
    选择recovery mode，回车确认； 
    在Recovery Menu中，选择“Root Drop to root shell prompt”，回车确认，如下图； 

    进入shell界面，使用passwd命令重新设定密码：passwd username
    若username忘记，可以cat  /etc/shadow  然后在一页左下角找到用户名。

    输入新密码； 
    再次确认新密码； 
    看到密码设定成功提示：passwd: password updated successfully； 
    重启系统进入GUI界面：sudo reboot；

3. 当在上面提到的shell 界面修改密码时，即使输入正确root仍然会出现read only问题。   
    网上给了两种方案，第一种chattr -i /etc/shadow 解锁用户名修改权限，chattr -i /etc/passwd解锁密码修改权限。但是这不行，尝试chmod 都不行。
    于是第二种方案，重新进入按e进入的恢复模式，ro改成rw，ctrl+x 直接进入shell界面。然后passwd username修改密码一气呵成，不过这里有没有需要之前chattr就不得而知了。也许是之前解锁过权限了，也许是不需要权限。
    以上


