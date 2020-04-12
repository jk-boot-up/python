import subprocess;
import time

class Sample2(object):
    def test_sample(self):
        f= open("t1.txt","w+")
        p = subprocess.Popen("nginx -V", stdout=f)
        f=p.communicate()[0]
        f.close()
        f2=open("t1.txt", "r")
        content = f2.read()
        print(content)


s1=Sample2()
s1.test_sample()