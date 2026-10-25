animals = {'cat', 'dog', 'fish', 'elephant', 'bird'}
animals.add('monkey')
print(animals)
# 运行结果: {'dog', 'monkey', 'cat', 'elephant', 'bird', 'fish'}
animals.update({'tiger', 'lion'})
print(animals)
# 运行结果: {'dog', 'monkey', 'cat', 'elephant', 'tiger', 'bird', 'lion', 'fish'}
