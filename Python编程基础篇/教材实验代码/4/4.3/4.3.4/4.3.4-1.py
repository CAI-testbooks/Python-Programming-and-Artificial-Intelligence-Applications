students_age = {'Tom': 18, 'Jerry': 20, 'Miffy': 22, 'Candy': 21, 'Kitty': 20, 'Micky': 18, 'Lily': 22}
print(students_age)
# 运行结果: {'Tom': 18, 'Jerry': 20, 'Miffy': 22, 'Candy': 21, 'Kitty': 20, 'Micky': 18, 'Lily': 22}

tmp = students_age.pop('Miffy')
print(tmp, students_age)
# 运行结果: 22 {'Tom': 18, 'Jerry': 20, 'Candy': 21, 'Kitty': 20, 'Micky': 18, 'Lily': 22}

tmp = students_age.pop('Miffy', 0)
print(tmp, students_age)
# 运行结果: 0 {'Tom': 18, 'Jerry': 20, 'Candy': 21, 'Kitty': 20, 'Micky': 18, 'Lily': 22}

tmp = students_age.pop('Miffy')
print(tmp, students_age)
# 运行结果: KeyError: 'Miffy'
