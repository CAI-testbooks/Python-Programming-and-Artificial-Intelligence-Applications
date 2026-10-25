student_name = input()
student_id = input()
student_grade = input()

print(student_name)
print(student_id)
print(student_grade)

# 使用 print() 输出学生信息
print(student_name, student_id, student_grade)

# 使用 print() 输出学生信息
print(student_name, student_id, student_grade, sep = ',')

# 使用 print() 输出学生信息
print("学生信息如下：")

print("姓名：", student_name)

print("学号：", student_id)

print("成绩：", student_grade)

# 默认每次输出后换行
print(0)
print(1)
print(2)

# 设置每次输出后不换行
print(0, end = '')
print(1, end = '')
print(2, end = '')
