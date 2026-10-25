animals = {'cat', 'dog', 'fish', 'elephant', 'bird'}
animals.add('monkey')
print(animals)
# 运行结果: {'dog', 'monkey', 'cat', 'elephant', 'bird', 'fish'}
animals.update({'tiger', 'lion'})
print(animals)
# 运行结果: {'dog', 'monkey', 'cat', 'elephant', 'tiger', 'bird', 'lion', 'fish'}




animals.pop()
print(animals)
# 运行结果: {'monkey', 'cat', 'elephant', 'tiger', 'bird', 'lion', 'fish'}
animals.remove('cat')
print(animals)
# 运行结果: {'monkey', 'elephant', 'tiger', 'bird', 'lion', 'fish'}

animals.remove('cat')
# 运行结果: KeyError: 'cat'
animals.discard('elephant')
print(animals)
# 运行结果: {'monkey', 'tiger', 'bird', 'lion', 'fish'}

animals.discard('elephant')
print(animals)
# 运行结果: {'monkey', 'tiger', 'bird', 'lion', 'fish'}
