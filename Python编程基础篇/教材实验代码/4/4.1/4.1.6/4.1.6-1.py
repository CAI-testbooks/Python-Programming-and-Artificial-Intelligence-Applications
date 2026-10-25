# len(obj)：返回元素个数。
animals = ['dog', 'cat', 'fish', 'bird', 'rabbit', 'hamster', 'turtle', 'snake', 'lizard']
print(len(animals))
# 运行结果: 9

# min(obj)：返回最小值。
numbers = [5, 12, 15, 22, 9, 18, 7, 34, 40]
print(min(numbers))
# 运行结果: 5

# max(obj)函数：返回最大值。
numbers = [5, 12, 15, 22, 9, 18, 7, 34, 40]
print(max(numbers))
# 运行结果: 40

# sum(iterable)：返回求和值。
numbers = [5, 12, 15, 22, 9, 18, 7, 34, 40]
print(sum(numbers))
# 运行结果: 162

# list.reverse()：将列表中的元素反向存放。
numbers = [5, 12, 15, 22, 9, 18, 7, 34, 40]
numbers.reverse()
print(numbers)
# 运行结果: [40, 34, 7, 18, 9, 22, 15, 12, 5]

# sorted(iterable, key=None, reverse=False)：返回一个新的排序后的列表，而原列表保持不变。
# key：排序函数，默认为None，这里暂不作详细介绍，可在需要时查阅相关资料；
# reverse：是否反向排序，默认为False；
numbers = [5, 12, 15, 22, 9, 18, 7, 34, 40]
sorted_numbers = sorted(numbers)
print(numbers, sorted_numbers)
# 运行结果: [5, 12, 15, 22, 9, 18, 7, 34, 40] [5, 7, 9, 12, 15, 18, 22, 34, 40]

# list.copy()：返回复制后的列表。
original_list = ['Chinese', 'English']
copied_list = original_list.copy()
print(f'原式列表: {original_list}, 复制列表: {copied_list}')
# 运行结果: 原式列表: ['Chinese', 'English'], 复制列表: ['Chinese', 'English']

# list.sort(key=None, reverse=False)：直接对原列表进行排序，不会返回任何值。
numbers = [5, 12, 15, 22, 9, 18, 7, 34, 40]
numbers.sort()
print(numbers)
# 运行结果: [5, 7, 9, 12, 15, 18, 22, 34, 40]
