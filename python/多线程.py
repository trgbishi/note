#一个简单的demo
import threading
def test():
    for i in range(0,5):
        th=threading.Thread(target=newthread,args=(i,))
        th.start()    


def newthread(i):  
    print(i)

test()


#setDaemon(true)，主线程结束时强制子线程结束
#setDaemon(false)，主线程结束时,子线程还会继续执行直到结束
#join，主线程执行到子线程时阻塞，等到所有子线程执行完毕后再继续执行主线程，可以设置timeout，单位是seconds