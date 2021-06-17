import queue
import threading
import time


def produce():
    for i in range(10):
        time.sleep(0.5)
        print('生產+++++麵包b{}'.format(i))
        q.put('b{}'.format(i))
def consumer():
    for i in range(100):
        time.sleep(1)
        #q.get()方法是一個阻塞方法
        print('買到-----麵包{}'.format(q.get()))

q = queue.Queue() #創建一個隊列 先進先出FIFO

p1 = threading.Thread(target=produce,name='p1')
c1 = threading.Thread(target=consumer,name='c1')
p1.start()
c1.start()
