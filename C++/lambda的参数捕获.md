### 显示捕获
显示捕获会列出我们打算使用的所在函数的变量
* 值捕获
```C++
void fun1()
{
	size_t v1=42;//
    //将v1拷贝到名为f的可调用对象
    auto f=[v1]{return v1;}
    v1=0;
    auto j=f();//j==42;f保存了我们创建它时v1的拷贝
}
```
* 引用捕获（请确保被引用的对象在lambda函数执行时是存在的
```C++
void fun2()
{
	size_t v1=42;
    //对象f2包含v1的引用
    auto f2 = [&v1]{return v1;}
    v1 = 0;
    auto j = f2();//j=0;f2保存v1的引用，而非拷贝
}
```
### 隐式捕获
隐式捕获让代码来推断我们要使用哪些变量
* 引用捕获
	[&]
* 值捕获
	[=]
* 混合捕获
	[&,c]
	[=,&os]
### 可变lambda
默认情况下，值拷贝不会改变参数值，但是可以通过加上关键字mutable来实现修改被捕获变量值。可变lambda能省略参数列表
```C++
void fun3()
{
	size_t v1 = 42;
    //f 可以改变它所捕获的变量的值
    auto f = [v1]() mutable {return ++v1;}
    v1 = 0;
    auto j = f();//j=43
}
```
一个引用捕获的变量是否可以修改取决于该引用指向的是const与否。