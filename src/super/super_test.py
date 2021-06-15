class A(object):

    def __init__(self, a, b):
        self._a = a
        self._b =b

    def print_me(self):
        print("a:{0}, b:{1}".format(self._a, self._b))

class B(A):

    def __init__(self, a, b):
        super(B, self).__init__(a, b)

    def print_me(self):
        print("aaaa:{0}, bbbb:{1}".format(self._a, self._b))

if __name__ == "__main__":
    b = B(10, 20)
    b.print_me()