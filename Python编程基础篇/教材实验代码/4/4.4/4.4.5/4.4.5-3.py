animals_1 = {'cat', 'dog', 'fish', 'elephant', 'bird'}
animals_2 = {'dog', 'monkey', 'lion', 'cat'}

# union() 求并集：把两个集合所有元素合并，自动去重
animals_union_1 = animals_1.union(animals_2)
print(animals_union_1)
# 运行结果: {'monkey', 'elephant', 'bird', 'fish', 'dog', 'cat', 'lion'}

# | 运算符，等价于 union()
animals_union_2 = animals_1 | animals_2
print(animals_union_2)
# 运行结果: {'monkey', 'elephant', 'bird', 'fish', 'dog', 'cat', 'lion'}
