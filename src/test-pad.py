import sys

class test(object):

    def __init__(self):
        self._a = "a"

    def call_me(self, param):
        y = self.__getattribute__("_a")
        print("y is:{}".format(y))
        ec2_tags = {}
        ec2_tags["env_name"] = "xyz"
        ec2_tags["env_type"] = "xyz"
        ec2_tags["xyz_groups"] = "xyz"
        if "env_name" in ec2_tags:
            print("done")
        else:
            print("not done")
        if int(param) == 0:
            print("passed 0")
            return 0
        elif int(param) == 1:
            print("passed 1")
            return 1
        else:
            print("passed unknown")
            return 100

if __name__ == "__main__":
    print((len(sys.argv)))
    params=[]
    for arg in sys.argv:
        params.append(arg)
    test1 = test()
    status = test1.call_me(params[1])
    sys.exit(status)

