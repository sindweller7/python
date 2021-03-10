import os
import shutil

def zipdir(dirpath):
    dirs = os.listdir(dirpath)
    for dir in dirs:
        if os.path.isdir(dir):
            filename = os.getcwd() +"\\" + dir + ".zip"            
            shutil.make_archive(filename, 'zip', dir)
            print(filename,"压缩完成")

zipdir(r".")
