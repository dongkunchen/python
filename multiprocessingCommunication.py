import os, time, multiprocessing

def create(x):
    for i in range(10):
        time.sleep(1)
        print('生產了+++++pid{} {}'.format(os.getpid(), i))
        x.put('pid{} {}'.format(os.getpid(),i))

def consumer(x):
    for i in range(10):
        time.sleep(0.3)
        print('消費了---------{}'.format(x.get(), i))

if __name__ == '__main__':
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=create,args=(q,))
    p2 = multiprocessing.Process(target=create,args=(q,))
    p3 = multiprocessing.Process(target=create,args=(q,))
    p1.start()
    p2.start()
    p3.start()

    c2 = multiprocessing.Process(target=consumer,args=(q,))
    c2.start()

