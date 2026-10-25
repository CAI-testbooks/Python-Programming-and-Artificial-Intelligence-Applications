a = [{'name': 'tom', 'age': 22},
     {'name': 'lily', 'age': 19},
     {'name': 'lucy', 'age': 20}]

result = sorted(a, key=lambda x:x['age'])
print(result)
# 输出：
# [{'name': 'lily', 'age': 19}, {'name': 'lucy', 'age': 20}, {'name': 'tom', 'age': 22}]
