hobbies = ['sing', 'dance', 'rap', 'basketball']
hobbies_tuple = tuple(hobbies)                # 将列表转为元组
print(type(hobbies_tuple), hobbies_tuple)
# 输出结果: <class 'tuple'> ('sing', 'dance', 'rap', 'basketball')

hobby1, hobby2, hobby3, hobby4 = hobbies_tuple
print(hobby1, hobby2, hobby3, hobby4)
# 输出结果: sing dance rap basketball

print('rap' in hobbies_tuple)                 # 判断元素是否在元组中
# 输出结果: True

print(hobbies_tuple.count('sing'))            # 统计元素出现次数
# 输出结果: 1

print(hobbies_tuple.index('rap'))             # 获取元素索引
# 输出结果: 2
