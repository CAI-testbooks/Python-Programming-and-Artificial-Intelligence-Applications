print(16/8)
print(16%-6)
print(-16%6)
x = 15
print(10<x<20)
print(10<x<12)
print((2+4)>(2+3))
print((20+10)<15<(25+15))
str1 = 'apple'
str2 = 'banana'
str3 = 'apple'
str4 = 'APPLE'
str5 = 'apple2'

print(str1 == str2)    # False
print(str1 != str2)    # True
print(str1 == str3)    # True
print(str1 == str4)    # False，区分大小写
print(str1 < str5)     # True
print(str1 < str2)     # True
print(str1 > str2)     # False
print(str1 <= str2)    # True
print(str1 >= str2)    # False
x=0
x+=4    # 等价于 x=x+4，此时 x 为 4
x-=1    # 等价于 x=x-1，此时 x 为 3
x*=5    # 等价于 x=x*5，此时 x 为 15
x/=3    # 等价于 x=x/3，此时 x 为 5.0
x%=3    # 等价于 x=x%3，此时 x 为 2.0
x**=4   # 等价于 x=x**4，此时 x 为 16.0
x//=3   # 等价于 x=x//3，此时 x 为 5.0
print(x)
print(True and False)
print(True and True)
print(True or False)
print(False or False)
print(not False)

print(0 and (10+15))    # 第一项是0，直接返回0，后面(10+15)不执行（短路）
print((12+5) or (20-10*2)) # 第一项非0，直接返回17，后面不执行（短路）

x = 10        # 10 的二进制为 00001010
y = 25        # 25 的二进制为 00011001
print(x & y)  # 按位与，00001000 → 8
print(x | y)  # 按位或，00011011 → 27
print(x ^ y)  # 按位异或，00010011 → 19
print(~ x)    # 按位取反，等价于 -x-1 → -11
print(x << 2) # 左移2位，相当于 x * 2² → 40
print(x >> 2) # 右移2位，相当于 x // 2² → 2
print('ab' in 'abc')
print('ac' in 'abc')
print('ba' not in 'abc')
a = 2
b = 3
c = 3
print(a is b)
print(b is c)
print(b is not c)
print(id(a))
print(id(b))
print(id(c))
