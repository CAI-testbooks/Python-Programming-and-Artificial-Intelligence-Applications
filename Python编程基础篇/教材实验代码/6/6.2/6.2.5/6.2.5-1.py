def 函数C():
    print("函数C开始执行。")
    # 这里抛出一个ValueError异常
    raise ValueError("这是一个ValueError异常，在函数C抛出。")
    print("函数C结束执行。")  # 这行不会运行，raise之后直接中断

def 函数B():
    print("函数B开始执行。")
    函数C()
    print("函数B结束执行。") # 不会运行，异常从C向上传递

def 函数A():
    print("函数A开始执行。")
    try:
        函数B()
    except ValueError as e:
        print(f"异常被函数A捕获：{e}")
    print("函数A结束执行。")

函数A()
