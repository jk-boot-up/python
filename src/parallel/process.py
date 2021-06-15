from multiprocessing import Process
import datetime


def f(name):
    print('hello', name)
    print(datetime.datetime.now())

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    p.terminate()
