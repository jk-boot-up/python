import abc

class Base11():

    @abc.abstractmethod
    def load_from_child(self):
        print("In base class")
        return
