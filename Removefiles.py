import os
import shutil
path=input("Put In The Path Of The File: ")
if os.path.exists(path):
    days=os.path.getmtime(path)
    os.listdir(path)
    os.walk(path)
    os.stat(path)
    if days>=30:
        os.remove(path)
    else:
        shutil.rmtree()
else:
    print("File Not Found")