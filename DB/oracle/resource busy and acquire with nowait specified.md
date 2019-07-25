1、用dba权限的用户查看数据库都有哪些锁
    select t2.username,t2.sid,t2.serial#,t2.logon_time
    from v$locked_object t1,v$session t2
    where t1.session_id=t2.sid order by t2.logon_time;

如：testuser 339 13545 2009-3-5 17:40:05
知道被锁的用户testuser，sid为339，serial#为13545

2、根据sid查看具体的sql语句，如果sql不重要，可以kill

    select sql_text from v$session a,v$sqltext_with_newlines b
    where DECODE(a.sql_hash_value, 0, prev_hash_value, sql_hash_value)=b.hash_value
    and a.sid=&sid order by piece;

查出来的sql，如： begin :id := sys.dbms_transaction.local_transaction_id; end;

3、kill该事务
    alter system kill session '339,13545';

[参考资料](http://www.cnblogs.com/chuanzifan/archive/2012/05/26/2519695.html)