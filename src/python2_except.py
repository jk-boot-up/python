
class Python2Except(object):

    def __init__(self):
        print("Created instance of: "+self.__class__.__name__)

    def trail_except_block(self, arg):
        try:
            if arg == "1":
                raise ValueError("Value Error")
            if arg == "2":
                raise IndexError("Index Error")
        except (ValueError, IndexError) as e:
            print(e)

    @classmethod
    def test_trail_except_block(cls):
        python2_except = Python2Except()
        python2_except.trail_except_block("1")
        python2_except.trail_except_block("2")

if __name__ == "__main__":
    Python2Except.test_trail_except_block()
