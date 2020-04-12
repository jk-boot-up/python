import subprocess
import os

class SpCall(object):
    def spcall(self):
        p = subprocess.check_output("/usr/local/bin/nginx -V |& tee /tmp/w1.txt", universal_newlines=True, shell=True)
        text=p.communicate()[0]

spc= SpCall()
spc.spcall()