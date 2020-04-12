import subprocess
import os

class SpCall(object):
    def spcall(self):
        p = subprocess.Popen(["nginx", "-V"], stdout=subprocess.PIPE, universal_newlines=True)
        text=p.communicate()[0]

spc= SpCall()
spc.spcall()