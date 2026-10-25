a = input('请输入第一个数：')
b = input('请输入第二个数：')
c = input('请输入第三个数：')
if a >= b:
    if a >= c:
        max = a  # a >= b且a >= c，所以a是最大的数
    else:
        max = c  # a >= b且c > a，所以c是最大的数
else:
    if b >= c:
        max = b  # b > a且b > c，所以b是最大的数
    else:
        max = c  # b > a且c > b，所以c是最大的数
print('最大的数是：', max)
