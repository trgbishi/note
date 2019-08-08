1. map对象内数据的改变，在线程间是可见的
2. 如果想要取消可见，可以将具体值赋给String,int等对象
3. 其它引用数据类型同map
4. 再想一下原理：引用数据类型传递的是地址，地址是固定值，而地址所指向的值可能是时刻改变的，即使是不同线程间，根据同一地址找到的内容都是一样的。而基本数据类型直接传递值，其它内存的值修改，对当前内存的值不影响
```java
    public static void main(String[] args) throws InterruptedException {
        Map<String, String> a = new HashMap<>();

        a.put("a", "a");
        new Thread(() -> {
            test(a);
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            test(a);
        }).start();
        Thread.sleep(3000);
        a.put("a", "b");
    }

    public static void test(Map<String,String> a ){
        System.out.println(a);
    }
```