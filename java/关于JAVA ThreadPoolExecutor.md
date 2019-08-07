## int corePoolSize
核心线程池线程数
核心线程不受keepAliveTime影响

## int maximumPoolSize
线程池最大大小

## long keepAliveTime
空闲线程的自动结束时间

## TimeUnit unit
keepAliveTime的单位

## BlockingQueue<Runnable> workQueue
ArrayBlockingQueue ：一个由数组结构组成的有界阻塞队列,FIFO
LinkedBlockingQueue ：一个由链表结构组成的有界阻塞队列,可以无界，FIFO
PriorityBlockingQueue ：一个支持优先级排序的无界阻塞队列
DelayQueue： 一个使用优先级队列实现的无界阻塞队列，只有当delay时间到了之后，才会出现头部，FIFO
SynchronousQueue： 一个不存储元素的阻塞队列，单工，有且仅有一个消费者在等待消息或者一个消息在等待被接收
LinkedTransferQueue： 一个由链表结构组成的无界阻塞队列，好像很nb，但是我看不懂，现在也不想看了
LinkedBlockingDeque： 一个由链表结构组成的双向阻塞队列,两端都可以进出

## ThreadFactory threadFactory
线程工厂，用该类来创建线程，一般为默认，即Executors.defaultThreadFactory()

## RejectedExecutionHandler handler
CallerRunsPolicy ： 直接在 execute 方法的调用线程中运行被拒绝的任务
AbortPolicy ： 丢弃被拒绝的任务，并抛出异常
DiscardPolicy ：丢弃被拒绝的任务，不抛出异常
DiscardOldestPolicy ：丢弃最早进来的任务，把该任务加入队列