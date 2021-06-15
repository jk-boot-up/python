from multiprocessing import Manager
from multiprocessing import Process, current_process
import time

class Test(object):

    def __init__(self):
        self.manager = Manager()
        self.namespace = self.manager.Namespace()
        self.process_list = []
        self.namespace.d=self.manager.dict()

    def print_me(self, ns, i):
        print("\nBefore:{0}, {1}, {2} ".format(current_process().name, i, ns.d))
        temp = i * i
        ns.d[i] =  temp
        print("\nAfter:{0}, {1}, {2} ".format(current_process().name, i, ns.d))
        time.sleep(5)
        return

    def spawn_processes(self):
        for i in range(5):
            p = Process(target=self.print_me, args=(self.namespace, i,))
            self.process_list.append(p)
            p.start()

        for i in self.process_list:
            i.join()

        print(self.namespace.d)

    def spawn_processes22(self):
        for i in range(5):
            p = Process(target=self.print_me, args=(self.namespace, i,))
            self.process_list.append(p)
            p.start()
            print("exitcode is:{0}".format(p.exitcode))
        while len(self.process_list) is not 0:
            for i in self.process_list:
                if not i.is_alive():
                    print("exitcode is:{0}".format(i.exitcode))
                    print("process:{0} is done, exit code:{1}".format(i.name, i.exitcode));
                    self.process_list.remove(i)
                    i.terminate()

        print(self.namespace.d)

if __name__ == "__main__":
    t = Test()
    t.spawn_processes22()





