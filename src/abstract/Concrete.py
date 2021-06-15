import abc

from base11 import Base11

class Concrete(Base11):

    def load_from_child(self):
        print("In Concrete class")
        return


if __name__ == "__main__":
    c=Base11()
    c.load_from_child()
    print("Is Sub class:{0} ".format(issubclass(Concrete, Base11)))
    print("Is Instance:{0} ".format(issubclass(Concrete, Base11)))
