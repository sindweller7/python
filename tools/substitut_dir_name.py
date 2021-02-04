# -*- coding: UTF-8 -*-
import os
import re

#设定修改名称的目录
path = r'D:\pythonProject\scrapy\financial\python_finacial'
#使用正则表达式提取出章节号
newname = r'.*?(\d+).*?'

for old_dir in os.listdir(path):
    #需要定义一个新的文件夹名称，不然无法为rename提供参数
    new_dir = re.findall(newname, old_dir)[0]
    os.rename(os.path.join(path, old_dir), os.path.join(path, new_dir))






    # if os.path.isfile(os.path.join(path, file)) == True:
    #     if file.find(oldname) > -1:
    #         new_name = file.replace(oldname, newname)
    #         os.rename(os.path.join(path, file), os.path.join(path, new_name))

