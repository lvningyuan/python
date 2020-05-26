import threading
g_num = 100
def test1(temp):
    global g_num
    mutex.acquire()
    for i in range(temp):
        g_num +=1
    mutex.release()
    print('g_num : %d' % (g_num))

def test2(temp):
    global g_num
    mutex.acquire()
    for i in range(temp):
        g_num +=1
    mutex.release()
    print('g_num : %d' % (g_num))

# 由于python代码是从上向下加载的，所以锁可以在外边创建
mutex = threading.Lock()

def main():
    #参数是一个元组
    t1 = threading.Thread(target=test1,args = (100,))
    t2 = threading.Thread(target=test2,args = (100,))
    t1.start()
    t2.start()

if __name__ =='__main__':
    main()
