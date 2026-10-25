fruits_number = {}            # 创建空字典
fruits_number['apple'] = 2    # key不存在 → 新增键值对
print(fruits_number)
# 输出：{'apple': 2}

tmp = fruits_number.setdefault('apple', 3)
print(tmp, fruits_number)
# 输出：2 {'apple': 2}
# apple已存在，返回旧值2，**不会修改原有value**

tmp = fruits_number.setdefault('banana', 3)
print(tmp, fruits_number)
# 输出：3 {'apple': 2, 'banana': 3}
# banana不存在，新增键值对，返回default的值3
