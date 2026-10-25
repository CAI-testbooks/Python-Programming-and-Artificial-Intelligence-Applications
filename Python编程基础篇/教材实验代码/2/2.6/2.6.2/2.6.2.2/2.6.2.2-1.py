#双分支
a = input('请输入第一个数：')
b = input('请输入第二个数：')
if a < b:
    max = b   # 如果b更大，则把b赋值给max
else:
    max = a   # 反之，即a更大，则把a赋值给max
print('较大的数是：', max)
