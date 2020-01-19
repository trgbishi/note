mysql8 以后的修改密码指令
alter user 'root'@'localhost' identified by 'Root@123';

一方面是修改密码的指令不能用之前版本的
set password = password('root');

另一方面是密码强度策略改了，需要加入特殊字符、大小写、数字等
