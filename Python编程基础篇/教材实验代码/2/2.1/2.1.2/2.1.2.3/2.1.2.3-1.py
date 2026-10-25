# 接下来通过示例讲解采用 f-string 的格式化输出。

# 默认格式不用指定格式描述符
name = "张三"
age = 25
print(f"我叫 {name}，今年 {age} 岁")

# content 内容可以为表达式
print(f"5 + 3 = {5 + 3}")

# content 内容可以为函数调用（关于函数的内容可以参考后续章节）
def greet(name):
    return f"你好，{name}"

print(f"{greet('张三')}")

# format() 方法的格式化操作也可以在此使用
pi = 3.14159
print(f"Pi = {pi:.2f}")   # 两位精度
print(f"{'word':*^10}")   # 设置最小宽度为10，居中显示，用 * 填充
