var = "I am global"

def my_function():
    global var        # 声明var是全局变量
    print(var)        # 使用全局变量
    var = "modify"    # 修改全局变量的值

my_function()        # 输出: I am global
print(var)           # 输出: modify
