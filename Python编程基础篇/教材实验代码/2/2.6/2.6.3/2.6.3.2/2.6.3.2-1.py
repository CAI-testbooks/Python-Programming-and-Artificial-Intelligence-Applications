n = int(input('请输入一个整数：'))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print('1到 {} 之和为：{}'.format(n, sum))
n = int(input('请输入一个整数：'))
result = 1
i = 1
while i <= n:
    result *= i
    i += 1
print('{} 的阶乘是：{}'.format(n, result))
a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
while b:
    a, b = b, a % b
print('最大公约数是：{}'.format(a))
