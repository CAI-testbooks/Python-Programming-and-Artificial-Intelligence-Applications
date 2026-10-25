# 方法2 for循环求最大公约数
a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
c = min(a, b)
for i in range(c, 0, -1):
    if a % i == 0 and b % i == 0:
        print('最大公约数是：', i)
        break

# continue示例，输出1~10的奇数
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
