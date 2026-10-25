vehicles = ['car', 'bicycle', 'motorcycle', 'bus', 'train']
vehicles.append('airplane')
print(vehicles)
# 运行结果: ['car', 'bicycle', 'motorcycle', 'bus', 'train', 'airplane']
# 当index>=0且index<len(list)时，在index的位置插入obj
vehicles.insert(2, 'scooter')
print(vehicles)
# 运行结果: ['car', 'bicycle', 'scooter', 'motorcycle', 'bus', 'train', 'airplane']

# 当index>=len(list)时，从尾部插入obj
vehicles.insert(10, 'subway')
print(vehicles)
# 运行结果: ['car', 'bicycle', 'scooter', 'motorcycle', 'bus', 'train', 'airplane', 'subway']

# 当index<0且abs(index)<len(list)时，从中间插入obj。如：-6表示从倒数第6个位置插入
vehicles.insert(-6, 'helicopter')
print(vehicles)
# 运行结果: ['car', 'bicycle', 'helicopter', 'scooter', 'motorcycle', 'bus', 'train', 'airplane', 'subway']

# 当index<0且abs(index)>=len(list)时，从头都插入obj
vehicles.insert(-20, 'rocket')
print(vehicles)
# 运行结果: ['rocket', 'car', 'bicycle', 'helicopter', 'scooter', 'motorcycle', 'bus', 'train', 'airplane', 'subway']
vehicles.remove('scooter')
print(vehicles)
# 运行结果: ['rocket', 'car', 'bicycle', 'helicopter', 'motorcycle', 'bus', 'train', 'airplane', 'subway', 'ship', 'boat', ['truck', 'van']]

vehicle_pop = vehicles.pop()
print(vehicle_pop, vehicles)
# 运行结果: ['truck', 'van'] ['rocket', 'car', 'bicycle', 'helicopter', 'motorcycle', 'bus', 'train', 'airplane', 'subway', 'ship', 'boat']

vehicle_pop = vehicles.pop(2)
print(vehicle_pop, vehicles)
# 运行结果: bicycle ['rocket', 'car', 'helicopter', 'motorcycle', 'bus', 'train', 'airplane', 'subway', 'ship', 'boat']

vehicles.pop(-5)
print(vehicles)
# 运行结果: ['rocket', 'car', 'helicopter', 'motorcycle', 'bus', 'airplane', 'subway', 'ship', 'boat']

vehicles.clear()
print(vehicles)
# 运行结果: []
