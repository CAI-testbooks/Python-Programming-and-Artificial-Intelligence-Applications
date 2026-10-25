#单分支
a = input('请输入第一个数：')
b = input('请输入第二个数：')
max = a          # 假设大的数是 a
if a < b:
    max = b      # 如果 a<b，则大的数是 b
print('较大的数是：', max)
