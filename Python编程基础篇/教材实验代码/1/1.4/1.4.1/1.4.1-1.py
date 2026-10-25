import os
print("你好，欢迎学习 Python!")

# 定义函数: 向某人打招呼
def say_hello(name):
    """向某人打招呼的函数 """
    message = "你好," + name + "!"
    print(message)

# 从这里开始执行程序
if __name__ == "__main__":
    say_hello("小明")
