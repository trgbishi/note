* __str__（self）方法不是用 Class().__str__()方式调用的！！！
另外，__method()确实是私有方法，但是__method__()好像不是

* __init__ ( self [,args...] )
构造函数
简单的调用方法: obj = className(args)

* __del__( self )
析构方法, 删除一个对象
简单的调用方法 : del obj

* _repr__( self )
转化为供解释器读取的形式
简单的调用方法 : repr(obj)

* __str__( self )
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)

* __cmp__ ( self, x )
对象比较
简单的调用方法 : cmp(obj, x)