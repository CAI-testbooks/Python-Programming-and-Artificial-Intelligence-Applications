import numpy as np

# 定义姓氏和名字数组
surnames = ('Smith', 'Galilei', 'Smith')
first_names = ('Tom', 'John', 'Mary')

# 使用lexsort进行排序,先按surnames 再按first_names
indices = np. lexsort ( (first_names, surnames) )
print("排序后索引:",indices)
# 输出:
# 排序后索引:[1 2 0]

# 根据排序后的索引重新排列姓氏和名字
sorted_names = [surnames [i] + ", " + first_names[i] for i in indices]
print("排序后的姓名列表:")
print(sorted_names)
# 输出:
# 排序后的姓名列表:
# ['Galilei, John', 'Smith, Mary', 'Smith, Tom']
