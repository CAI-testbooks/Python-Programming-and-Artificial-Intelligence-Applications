# import 模块名
import socket
c = socket.socket()  # 使用方法: 模块名.方法()

# 导入模块的单个对象：

# from 模块名 import 对象 [as 别名]
from os import mkdir
# c = mkdir(xxx)

from os import mkdir as mk
# c = mk(xxx)

# 导入模块的多个对象：

# from 模块 import 对象1, 对象2...
from time import ctime, asctime

# 导入模块的全部对象：

# from 模块 import *
from math import *
