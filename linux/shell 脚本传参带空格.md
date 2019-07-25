    shell脚本传参是通过空格隔开的，所以一旦带空格就会出错
    这时可以通过加双引号解决
    如：
    test.py
        #!/usr/bin/sh
        echo $1
        echo $2
        echo "$3"
        echo $4

    sh test.py 1 2 "3 3" 4
    
    output:
        1
        2
        3 3
        4
    
    带双引号的参数，脚本内调用也需要加""，如上面的"$3"
    