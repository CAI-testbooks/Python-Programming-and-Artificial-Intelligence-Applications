context = 'Python is my favorite language.'
print(context.startswith('Python'))        # 判断是否以 'Python' 开始
# 运行结果: True
print(context.startswith('Python', 10))    # 指定从第10个位置开始判断
# 运行结果: False
print(context.endswith('language.'))       # 判断是否以 'language.' 结束
# 运行结果: True
