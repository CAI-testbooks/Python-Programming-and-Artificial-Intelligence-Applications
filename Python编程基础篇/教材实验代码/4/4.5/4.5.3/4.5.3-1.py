language = 'Chinese,English,French,Chinese,German,Japanese'

print(language.find('Chinese'))                # 0，第一次出现下标
print(language.find('Chinese', 1))            # 23，从下标1往后找
print(language.find('Chinese', 1, 22))        # -1，在[1,22)区间没找到

print(language.rfind('Chinese'))              # 23，最后一次出现
print(language.rfind('Chinese', 0, 22))       # 0，在[0,22)区间，最靠右的Chinese在0

print(language.index('Chinese'))              # 0
# print(language.index('Chinese', 1, 22))     # 找不到，报错 ValueError: substring not found

print(language.rindex('Chinese', 0, 30))      # 23

print(language.count('Chinese'))              # 2，一共出现2次
