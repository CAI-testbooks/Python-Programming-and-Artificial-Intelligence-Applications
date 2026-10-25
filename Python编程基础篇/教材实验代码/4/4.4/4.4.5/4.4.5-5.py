animals_1 = {'cat', 'dog', 'fish', 'elephant', 'bird'}
animals_2 = {'dog', 'monkey', 'lion', 'cat'}

# symmetric_difference() 对称差集：只在其中一个集合里出现的元素，去掉两边共有的
animals_symmetric_difference_1 = animals_1.symmetric_difference(animals_2)
print(animals_symmetric_difference_1)
# 运行结果: {'monkey', 'elephant', 'bird', 'lion', 'fish'}

# ^ 运算符，等价于 symmetric_difference()
animals_symmetric_difference_2 = animals_1 ^ animals_2
print(animals_symmetric_difference_2)
# 运行结果: {'monkey', 'elephant', 'bird', 'lion', 'fish'}
