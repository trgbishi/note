
### shutdown() 
    停止接收任务（即在之后再submit，会报RejectedExecutionException）
    将等待的与正在进行的任务进行完

### shutdownNow()
    停止接收任务
    忽略等待任务
    尝试中断任务
    返回未执行任务list

### awaitTermination(long timeOut, TimeUnit unit)
    阻塞当前线程
    继续接收任务
    继续执行等待的与正在进行的任务
    超时时间到则终止
    返回线程池是否终止bool


> 优雅关闭用shutdown

> 暴力关闭用suhtdownnow

> awaitTermination好像没用啊，测试发现除了阻塞外没有任何作用。即使连等待线
程都执行完了，依然是false状态，即线程池未关闭。所以其实是用来监测线程池状态的？

测试代码：
```
    import java.util.concurrent.Executors;
    import java.util.concurrent.ScheduledExecutorService;
    public class Test {
    
        public static void main(String[] args) throws InterruptedException {
            ScheduledExecutorService service = Executors.newScheduledThreadPool(1);
            service.submit(()->{
                try {
                    Thread.sleep(2000);
                    System.out.println("thread 1 run success");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
    
            service.submit(()->{
                try {
                    Thread.sleep(2000);
                    System.out.println("thread 2 run success");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
    
    //        service.shutdown();
            System.out.println(service.shutdownNow());
    
    //        while (!service.awaitTermination(1000, TimeUnit.MILLISECONDS)){
    //            System.out.println("thread pool not terminated");
    //        }
    
            service.submit(()->{
                try {
                    Thread.sleep(2000);
                    System.out.println("thread 3 run success");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
            System.out.println("that's all");
        }
    
    }
```    
[参考资料](https://blog.csdn.net/u012168222/article/details/52790400)
