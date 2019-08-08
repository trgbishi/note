>吃早餐看见的

[原文](https://mp.weixin.qq.com/s?__biz=MzI3ODcxMzQzMw==&mid=2247483993&idx=1&sn=9ff0f38c4be41f5030d2fa9acc283dd6&scene=21#wechat_redirect)

线程内修改tmp值，对线程外没有影响
```java
    public class Test {
        public static int tmp = 0;

        public static void main(String[] args) {
            new Thread(()->{
                    try{
                        Thread.sleep(1000);
                    }catch (InterruptedException e){
                        e.printStackTrace();
                    }
                    tmp = 1;
            }).start();

            while (tmp==0){
            
            }
            System.out.println("tmp changed");

        }
    }
```

此时在while(tmp==0)的循环内输出tmp值，理论上会一直是输出0，然后最后输出的 "tmp changed" 当然不会输出咯
```java
	while (tmp==0){
		System.out.println(tmp);
	}
```
然而却会走出循环，即线程外的tmp值也改变了。在线程内的修改对线程外可见，但是定义变量时并没有加volatile，凭什么可见？
这时候点开println方法的源码
```java
    public void println(int x) {
        synchronized (this) {
            print(x);
            newLine();
        }
    }
```    
发现有一个同步操作，synchronized(this),使变量可见了。
因此，在没有声明volatile时，想要可见，还可以直接：
```java
    while (tmp==0){
        synchronized ((Object)tmp){

        }
    }
```