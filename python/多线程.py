#一个简单的demo
import threading
def test():
    for i in range(0,5):
        th=threading.Thread(target=newthread,args=(i,))
        th.start()    


def newthread(i):  
    print(i)

test()