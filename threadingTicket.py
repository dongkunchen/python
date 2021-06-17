import threading
import time

#多個現成可以同時操作一個全局變量
ticket = 20

#創建一把鎖
lock = threading.Lock()

def sell_ticket():
    global ticket
    while True:
        #加同步鎖
        lock.acquire()
        if ticket > 0:
            time.sleep(1)
            ticket -= 1
            #釋放鎖
            lock.release()
            print('{}賣出一張票,還剩{}張'.format(threading.current_thread().name, ticket))
        else:
            #釋放鎖
            lock.release()
            print('票賣完了')
            break

t1 = threading.Thread(target=sell_ticket,name='線程1')
t2 = threading.Thread(target=sell_ticket,name='線程2')
t1.start()
t2.start()