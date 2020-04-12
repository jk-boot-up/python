import subprocess;
import os;
from subprocess import check_output

class TestMe(object):
    def test_output(self):
        p=subprocess.Popen("/usr/local/bin/nginx -V", stdout=subprocess.PIPE, shell=True, universal_newlines = True,)
        configLines=[]
        while True:
            rc = p.poll()
            line = p.stdout.readline()
            if line != "":
                configLines.append(p.stdout.readline())
            rc=p.poll()
            if rc != None:
                break
        return configLines






test_1 = TestMe()
conf = test_1.test_output()
print(conf)

