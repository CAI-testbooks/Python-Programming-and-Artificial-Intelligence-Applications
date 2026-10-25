def student_info(name, age, major):
    return {"name": name, "age": age, "major": major}

student = student_info("Alice", 21, "Computer Science")
print(student)
# 输出: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}
