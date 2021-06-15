#!/usr/bin/python

import subprocess
from subprocess import Popen

def hello():
    my_process = Popen("python s1.py", stdout=subprocess.PIPE, shell=True)
    my_process.wait()
    s = None
    for line in my_process.stdout:
        s = line.strip()
    print("value received is:{}".format(str(s).strip()))

if __name__ == "__main__":
    hello()

