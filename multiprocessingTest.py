import multiprocessing, time, os

def dance(n):
    for i in range(n):
        time.sleep(0.5)
        print('正在跳舞,pid{}'.format(os.getpid()))

def sing(m):
    for i in range(m):
        time.sleep(0.5)
        print('正在唱歌,pid{}'.format(os.getpid()))

if __name__ == '__main__':
    print('主進程的pid{}'.format(os.getpid()))
    #創建了兩個進程
    #target用來表示執行的任務
    #args 用來傳參 類型是一個元組args=(50,)
    p1 = multiprocessing.Process(target=dance, args=(100,))
    p2 = multiprocessing.Process(target=sing, args=(100,))

    p1.start()
    p2.start()