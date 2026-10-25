animals_1 = {'cat', 'dog', 'fish', 'elephant', 'bird'}
animals_2 = {'dog', 'monkey', 'lion', 'cat'}
animals_3 = {'fish', 'elephant', 'bird'}

# isdisjoint() 判断两个集合是否**没有任何交集（完全不相交）**
print(animals_1.isdisjoint(animals_2))  # 输出: False，存在共同元素 cat、dog
print(animals_2.isdisjoint(animals_3))  # 输出: True，两个集合没有相同元素
