for letter in 'Python':
    print('当前字母：', letter)
for i in range(5):
    print(i)
for i in range(5, 9):
    print(i)
for i in range(2, 11, 2):
    print(i)
for i in range(10, 1, -2):
    print(i)
n = int(input('请输入一个整数：'))
sum = 0
for i in range(1, n + 1):
    sum += i   # sum = sum + i
print('1到 {} 之和为：{}'.format(n, sum))
n = int(input('请输入一个整数：'))
result = 1
for i in range(1, n + 1):
    result *= i  # result = result * i
print('{} 的阶乘是：{}'.format(n, result))
