def register_student(name, age, *hobbies):
    print(f"Student Name: {name}")
    print(f"Student Age: {age}")
    print("Student Hobbies:")
    for hobby in hobbies:
        print(f"- {hobby}")

# 传递不同数量的爱好
register_student("Alice", 21, "Reading", "Swimming", "Cycling")
register_student("Bob", 22, "Football")
