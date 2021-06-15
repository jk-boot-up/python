from queue import Queue
class QSample:

    def __init__(self):
        self._q = Queue()


    def print_me(self):
        while not self._q.empty():
            print(f"element is:{self._q.get(False)}")

if __name__ == "__main__":
    q = QSample()
    q._q.put("Hello")
    q._q.put("World")
    q.print_me()
