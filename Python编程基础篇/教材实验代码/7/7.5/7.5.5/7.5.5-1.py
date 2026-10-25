import os

path = os.path.join("folder", "file.txt")   # 路径拼接，自动适配Windows/Linux分隔符
name = os.path.basename(path)              # 获取文件名，结果："file.txt"
folder = os.path.dirname(path)             # 获取目录路径，结果："folder"
