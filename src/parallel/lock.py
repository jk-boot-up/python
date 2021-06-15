from multiprocessing import Process, Lock
import getopt

def f(l, i):
    l.acquire()
    print('hello world', i)
    print("criteria: {0} ".format(i))
    l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()