#多分支
a = input('请输入第一个数：')
b = input('请输入第二个数：')
c = input('请输入第三个数：')
if a >= b and a >= c:
    max = a   # 如果a是最大的数，则把a赋值给max
elif b >= c: # 如果a不是最大的数，那么最大的数肯定在b和c里，只需比较b和c的大小即可
    max = b
else:
    max = c
print('最大的数是：', max)
