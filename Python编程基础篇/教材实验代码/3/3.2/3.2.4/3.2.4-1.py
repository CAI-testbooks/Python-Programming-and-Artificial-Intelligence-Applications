def register_student(name, age=18, *hobbies, **extra_info):
    print(f"Student Name: {name}")
    print(f"Student Age: {age}")
    print("Student Hobbies:")
    for hobby in hobbies:
        print(f"- {hobby}")
    print("Additional Information:")
    for key, value in extra_info.items():
        print(f"- {key}: {value}")

# 调用时传入不同类型的参数
register_student("Alice", 21, "Reading", "Swimming", major="Computer Science", grade="A", city="New York")

register_student("Bob", 22, "Football", major="Mathematics", grade="B", city="Los Angeles")
