animals_1 = {'cat', 'dog', 'fish', 'elephant', 'bird'}
animals_2 = {'fish', 'elephant', 'bird'}

print(animals_1.issubset(animals_2)) # False，animals_1不全在animals_2里面
print(animals_2.issubset(animals_1)) # True，animals_2所有元素都在animals_1
print(animals_2.issubset(animals_2)) # True，集合是自身的子集

print(animals_1 <= animals_2) # False
print(animals_2 <= animals_1) # True

print(animals_2 < animals_2)  # False，集合等于自己，不是真子集
print(animals_2 < animals_1)  # True，animals2是animals1的真子集

print(animals_1.issuperset(animals_2)) # True，animals_1包含animals_2全部元素
print(animals_2.issuperset(animals_1)) # False

print(animals_1 >= animals_2) # True
print(animals_2 >= animals_1) # False

print(animals_1 >= animals_1) # True，自己是自己的超集
print(animals_1 > animals_1)   # False，不是真超集
print(animals_1 > animals_2)   # True，animals1是animals2的真超集
