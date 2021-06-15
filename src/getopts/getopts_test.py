#!/usr/bin/python
import getopt
import sys

class GetOpts(object):
    def __init__(self):
        pass

    def test(self):
        try:
            argv = sys.argv[1:]
            opts, args = getopt.getopt(argv, "", ["env=", "dep_groups="])
            print("Arguments parsed successfully: " + ", ".join(map(str, opts)))
            args_dict = dict(opts)
            v1 = args_dict["--env"]
            v2 = args_dict["--dep_groups"]
            print("v1 is: {0}".format(v1))
            print("v2 is: {0}".format(v2))
            for opt, arg in opts:
                if opt == "--env":
                    print(arg)
                elif opt == "--dep_groups":
                    print(arg)
            for tuple1 in opts:
                if tuple1[0] == "--env":
                    print(tuple1[1])
                elif tuple1[0] == "--dep_groups":
                    print(tuple1[1])
        except getopt.GetoptError as err:
            print("Failed to parse arguments")
            print(err)
            sys.exit(5)

if __name__ == "__main__":

    print("sys args are:{0}".format(sys.argv))
    parser = GetOpts()

    parser.test()