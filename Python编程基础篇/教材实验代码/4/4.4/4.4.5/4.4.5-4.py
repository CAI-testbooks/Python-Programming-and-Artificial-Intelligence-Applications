animals_1 = {'cat', 'dog', 'fish', 'elephant', 'bird'}
animals_2 = {'dog', 'monkey', 'lion', 'cat'}

# difference() 求差集：在animals_1里，但不在animals_2中的元素
animals_difference_1 = animals_1.difference(animals_2)
print(animals_difference_1)
# 运行结果: {'bird', 'elephant', 'fish'}

# - 减号运算符，等价于 difference()
animals_difference_2 = animals_1 - animals_2
print(animals_difference_2)
# 运行结果: {'bird', 'elephant', 'fish'}
