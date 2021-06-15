

class Params(object):

    def __init__(self):
        pass

    def test_me(self, results=True):
        results = False
        return
    def test(self):
        success = True
        self.test_me(success)
        print(success)

    def test_list(self, results_holder=None):
        results = False
        if results_holder is not None:
            results_holder.append(True)
        return
    def test_passing_list(self):
        success_holder = []
        self.test_list(success_holder)
        print(success_holder)

if __name__ == "__main__":
    params = Params()
    #params.test()
    params.test_passing_list()
