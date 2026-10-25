import os

os.path.exists("file.txt")     # 判断路径是否存在（文件/文件夹都算）
os.path.isfile("file.txt")     # 判断是否是普通文件
os.path.isdir("folder")        # 判断是否是文件夹（目录）
