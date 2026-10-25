language = ['Python', 'Java', 'C++', 'Ruby', 'PHP']
for x in language:
    print(x, end=' ')
# 运行结果: Python Java C++ Ruby PHP
# 等价于如下代码：
it = iter(language)        # ① iter(可迭代对象)，返回迭代器
while True:
    try:
        x = next(it)       # ② next(迭代器)，取出下一个元素
        print(x, end=' ')
    except StopIteration:   # ③ 迭代器无元素时抛出StopIteration异常
        break               # 捕获异常，退出循环
# 运行结果: Python Java C++ Ruby PHP
