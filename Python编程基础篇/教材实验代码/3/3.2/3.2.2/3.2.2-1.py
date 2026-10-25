def register_student(name, age, gender):
    print(f"Student Name: {name}")
    print(f"Student Age: {age}")
    print(f"Student Gender: {gender}")

# 使用关键字参数来指定参数值
register_student(age=20, name="Charlie", gender="Male")
