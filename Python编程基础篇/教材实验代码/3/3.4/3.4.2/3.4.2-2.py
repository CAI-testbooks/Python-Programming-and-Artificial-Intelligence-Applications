var = "I am global"

def my_function():
    var = "I am local"  # 局部变量和全局变量同名
    print(var)           # 优先使用局部变量

my_function()  # 输出: I am local
