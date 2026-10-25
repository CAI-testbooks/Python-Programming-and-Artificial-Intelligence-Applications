animals_1 = {'cat', 'dog', 'fish', 'elephant', 'bird'}
animals_2 = {'dog', 'monkey', 'lion', 'cat'}

# intersection() 求交集：两个集合**都存在**的元素
animals_intersection_1 = animals_1.intersection(animals_2)
print(animals_intersection_1)
# 运行结果: {'dog', 'cat'}

# & 运算符，等价于 intersection()
animals_intersection_2 = animals_1 & animals_2
print(animals_intersection_2)
# 运行结果: {'dog', 'cat'}
