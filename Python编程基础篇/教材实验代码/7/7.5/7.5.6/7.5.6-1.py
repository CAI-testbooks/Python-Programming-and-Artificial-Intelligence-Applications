import os

# os.walk 遍历当前目录 "."，递归遍历所有子文件夹
for dirpath, dirnames, filenames in os.walk("."):
    print("当前目录：", dirpath)
    print("子目录：", dirnames)
    print("文件列表：", filenames)
