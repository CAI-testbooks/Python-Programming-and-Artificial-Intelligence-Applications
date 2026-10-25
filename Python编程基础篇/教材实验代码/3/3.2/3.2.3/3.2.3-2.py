def register_student(name, age, **extra_info):
    print(f"Student Name: {name}")
    print(f"Student Age: {age}")
    print("Additional Information:")
    for key, value in extra_info.items():
        print(f"- {key}: {value}")

# 传递多个额外信息
register_student("Alice", 21, major="Computer Science", grade="A", city="New York")
register_student("Bob", 22, major="Mathematics", grade="B", city="Los Angeles")
