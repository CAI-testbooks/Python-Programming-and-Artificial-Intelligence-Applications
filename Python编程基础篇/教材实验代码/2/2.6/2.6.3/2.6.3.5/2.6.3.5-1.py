# 求1!+2!+3!+...+n!
n = int(input('请输入一个整数：'))
total_sum = 0
for i in range(1, n + 1):
    factorial = 1                 # 初始化阶乘结果
    for j in range(1, i + 1):     # 内层循环计算当前数的阶乘
        factorial *= j
    total_sum += factorial        # 将当前阶乘结果加到总和中
print("'1! + 2! + 3! + ... + {}!' 的结果是：{}".format(n, total_sum))
# 找出2~100之间所有素数
for num in range(2, 101):                # 外层循环遍历2到100的每个数
    for i in range(2, num - 1):          # 内层循环检查是否有因子
        if num % i == 0:                 # 如果有因子，说明不是素数
            break                        # 退出内层循环
    else:                                 # 正常退出内层循环，也就是没有找到因子，说明是素数
        print(num, end = ' ')
