# 列表推导式生成列表：1~10的平方
square_num = [i ** 2 for i in range(1, 11)]
print(square_num)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(square_num[:])
print(square_num[0:])
print(square_num[:len(square_num)])
# 全部输出：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(square_num[:8])       # stop=8，取索引0~7 → [1, 4, 9, 16, 25, 36, 49, 64]
stop = -7
print(square_num[:stop])
print(square_num[:len(square_num)+stop])
# stop=-7，len=10，10 + (-7)=3，取0~2 → [1,4,9]

print(square_num[2:])       # start=2，从索引2一直到末尾 → [9, 16, 25, 36, 49, 64, 81, 100]

start = -5
print(square_num[start:])
print(square_num[len(square_num)+start:])
# start=-5，10 + (-5)=5，从索引5开始 → [36, 49, 64, 81, 100]

print(square_num[2:8])   #索引2~7 → [9, 16, 25, 36, 49, 64]
print(square_num[2:2])   #start和stop相等，取不到元素 → []
print(square_num[8:2])   #step默认+1，要求start<stop；8>2，方向矛盾 → []

start = -7
stop = -5
print(square_num[start:stop:])
# start=-7 → 10-7=3；stop=-5 →10-5=4；取索引3 → [16,25]
print(square_num[len(square_num) + start:len(square_num) + stop])
# len=10，10-7=3，10-5=4，等价写法，同样输出[16,25]

print(square_num[8:2:-2])
# start=8，stop=2，step=-2，向左取：索引8 →6 →4
# 8:81，6:49，4:25 → [81, 49, 25]

start = -5   #10-5=5
stop = -7    #10-7=3
print(square_num[start:stop:-1])
# start=5，stop=3，step=-1，向左取索引5 →4
# 索引5=36，索引4=25 → [36, 25]
print(square_num[len(square_num)+start:len(square_num)+stop:-1])
#等价写法，同样输出[36, 25]

print(square_num[::-1]) # 常用！反转整个列表 → [100, 81, 64, 49, 36, 25, 16, 9, 4, 1]
print(square_num[1::2])# start=1，到末尾，步长2，取奇数索引：1,3,5,7,9 → [4, 16, 36, 64, 100]
