context = 'I love Python, Python is my favorite language.'
print(context.replace('Python', 'Java', 1)) 
# count=1：只替换第一个匹配的Python
# 输出：I love Java, Python is my favorite language.

print(context.replace('Python', '')) 
# new为空字符串，等价于删除这个子串
# 输出：I love , is my favorite language.
