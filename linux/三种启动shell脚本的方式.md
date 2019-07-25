1../test.sh
	该方式会以test.sh的第一行指定的解释器执行该脚本

2.sh test.sh
	直接运行解释器sh，至于脚本第一行指定的解释器此时不起作用
	还有解释器如
    Bourne Shell（/usr/bin/sh或/bin/sh）
    Bourne Again Shell（/bin/bash）
    C Shell（/usr/bin/csh）
    K Shell（/usr/bin/ksh）
    Shell for Root（/sbin/sh）

3.test.sh
	当环境变量的PATH指定的各目录下有该脚本则执行，没有就报错