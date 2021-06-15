import os
from os import path
import shutil
import glob

def test_is_symlink():
    if path.islink("/Users/kondurj/jk/git-hub-jk-boot-up/python/src"):
        print("It is a link")
    if path.isdir("/Users/kondurj/jk/git-hub-jk-boot-up/python/src"):
        print("It is a directory")

    if path.isdir("/Users/kondurj/jk/git-hub-jk-boot-up/python/src/dummy"):
        print("trying to delete")
        shutil.rmtree("/Users/kondurj/jk/git-hub-jk-boot-up/python/src/dummy")
        print("deleted")
def test_path():
    if os.path.exists("active.tmp"):
        print("path exists")
        os.remove("active.tmp")
        print("deleted active.tmp")

def test_dir():
    active_path = os.path.join("/Users/kondurj/jk/git-hub-jk-boot-up/python/src", "active")
    print(active_path)

def test_glob_remove():
    f="/Users/kondurj/jk/git-hub-jk-boot-up/python/src/test-dirs/nginx-1-1-1.txt"
    dirs = glob.glob(os.path.join("/Users/kondurj/jk/git-hub-jk-boot-up/python/src/test-dirs", "nginx-*"))
    one = "/Users/kondurj/jk/git-hub-jk-boot-up/python/src/test-dirs/nginx-1"
    print(dirs)
    one = None
    if one in dirs:
        dirs.remove(None)
        print("element removed is:", one)
    print(dirs)



if __name__ == "__main__":
    test_glob_remove()