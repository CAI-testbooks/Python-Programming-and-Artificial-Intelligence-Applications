import os

os.mkdir("new_folder")      # 创建单层目录（上级目录必须已经存在）
os.makedirs("a/b/c")        # 创建多层嵌套目录，不存在的父目录自动创建
os.rmdir("new_folder")      # 删除空目录，文件夹里面有文件会报错
