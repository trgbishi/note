	public static volatile int aa = 0;
    public static void main(String[] args) {
        CountDownLatch countDownLatch = new CountDownLatch(4);
        for (int i = 0; i < 4; i++) {
            new Thread(() -> {
                System.out.println(Thread.currentThread().getName());
                try {
                    Thread.sleep(10000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println(Thread.currentThread().getName() + " end");
                aa++;
                countDownLatch.countDown();
            }).start();
        }
        System.out.println("await");
        try {
            countDownLatch.await(4, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(aa);
        System.out.println("all end");
        try {
            countDownLatch.await(10, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(aa);
    }
## 总结：
1. CountDownLatch的初始构造参为阈值，每次到线程末尾 countDown一次
2. 理论上线程会直接略过，到达线程执行体外，不阻塞，继续进行后续的操作。因此会出现线程里面进行的IO操作，但是操作得到的值是后续操作需要的。此时利用await阻塞一定时间，当且仅当countDown把构造参传入的阈值减为0后或达到await参数填入的超时时间，打开阻塞通道。
3. 需要注意countDown是否能把阈值减完，或者当线程运行时间需要很长就有必要设置比较大的超时时间。
4. 超时时间应该是注意用于 IO操作无法获取值或者其他异常情况导致长时间阻塞的情况，而不应该限制正常的线程执行时间以阻挡线程运行