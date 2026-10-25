def fact(n):
    if n == 0:          # 递归终止条件
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))   # 输出: 120
