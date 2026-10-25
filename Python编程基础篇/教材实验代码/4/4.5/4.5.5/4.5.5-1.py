language = 'Chinese,English,French,Chinese,German,Japanese'
print(language.split(','))        # 使用逗号分割
# 运行结果: ['Chinese', 'English', 'French', 'Chinese', 'German', 'Japanese']
print(language.split(',', 2))     # 使用逗号分割，最多分割2次
# 运行结果: ['Chinese', 'English', 'French,Chinese,German,Japanese']
print(language.rsplit(',', 2))    # 使用逗号分割，最多分割2次
# 运行结果: ['Chinese,English,French,Chinese', 'German', 'Japanese']

context = 'Python is my favorite language. Python is easy to learn.'
print(context.partition('is'))    # 从左开始查找
# 运行结果: ('Python ', 'is', ' my favorite language. Python is easy to learn.')
print(context.rpartition('is'))   # 从右开始查找
# 运行结果: ('Python is my favorite language. Python ', 'is', ' easy to learn.')

context = 'Python is my favorite language.\nPython is easy to learn.'
print(context.splitlines())        # 不保留换行符
# 运行结果: ['Python is my favorite language.', 'Python is easy to learn.']
