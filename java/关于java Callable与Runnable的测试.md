一个demo，测试了下Callable,Runnable，理清楚相互间的关系。
Callable是有返回值的Runnable，即回调。<br>
当需要线程执行结果时，可以将Callable对象作为唯一构造参数，来定义FutureTask对象<br>
当使用futureTask.get()时，会阻塞，直到futureTask里的线程执行完毕并返回<br>

另外有一点，执行runnable或callable时，不要定义线程池来执行，因为执行完线程，线程池会等待新线程，而不会关闭程序。
正确做法是开一个线程，将runnable或callable放进去。
```java
    public class Test {
    
        public static void main(String[] args) {
            testCallable();
    //        testRunnable();
        }
    
        private static void testRunnable() {
            new Thread(() -> System.out.println("2333")).run();
        }
    
        private static void testCallable() {
            FutureTask<Integer> futureTask = new FutureTask(new Callable() {
                @Override
                public Object call() throws Exception {
                    Thread.sleep(3000);
                    return 10;
                }
            });
            // 等价于lambda形式
    //        FutureTask<Integer> futureTask = new FutureTask(()->{
    //                Thread.sleep(3000);
    //                return 10;
    //        });
    
            /**
             * Executors.newSingleThreadExecutor() 是一个线程数量为1的线程池
             * 当前执行的线程执行完，线程池不会结束，即程序不会结束
             * 在不关闭程序的情形下，再次new 某类，可能会造成已有线程池没有回收
             * 如果有多个线程被提交，将会排队
             */
    //        Executor executor = Executors.newSingleThreadExecutor();
    //        executor.execute(futureTask);
    
            /**
             * 如果只需要执行一次，就不需要线程池了，单开个线程执行即可
             */
            new Thread(futureTask).start();
    
    
            System.out.println("before get");
            try {
                System.out.println(futureTask.get());
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (ExecutionException e) {
                e.printStackTrace();
            }
            System.out.println("after get");
            return;
        }
    
    }
```