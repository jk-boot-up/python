from multiprocessing import Process

def f1(x):
    print('hello', x)
    temp1=0
    for i in range(10000):
        temp1=temp1+2
        print("{}:{}\n".format(x, temp1))

def f2(y):
    print('hello', y)
    temp2=0
    for i in range(10000):
        temp2=temp2+3
        print("{}:{}\n".format(y, temp2))

if __name__ == '__main__':
    a1="even"
    a2="odd"
    p1 = Process(target=f1, args=(a1,))
    p2 = Process(target=f2, args=(a2,))
    print("Starting parallel processing")
    p1.start()
    p2.start()
    print("Triggered parallel processing")
    p1.join()
    print("p1 completed")
    p2.join()
    print("p2 completed")
    print("DONE")