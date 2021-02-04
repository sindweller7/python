# -*- coding: UTF-8 -*-
import os
import re

# 设定文件存放的路径
path = r'F:\Downloads\Downloads\1'
# .*后面不能有问号，负责无法匹配内容
newname = r'【微信yes0000no】(.*)'

for old_name in os.listdir(path):
    print(old_name)
    # 需要定义一个新的文件名称，不然无法为rename提供参数
    new_name = re.findall(newname, old_name)[0]
    print(new_name)
    os.rename(os.path.join(path, old_name), os.path.join(path, new_name))