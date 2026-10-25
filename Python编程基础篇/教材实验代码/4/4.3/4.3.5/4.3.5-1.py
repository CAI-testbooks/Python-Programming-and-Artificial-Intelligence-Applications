students_telephone = {"Alice": "123-456-7890", "Bob": "234-567-8901",
"Charlie": "345-678-9012"}

students_telephone['Alice'] = "123-456-0000"  # 修改Alice的电话号码
print(students_telephone)
# 运行结果: {'Alice': '123-456-0000', 'Bob': '234-567-8901', 'Charlie': '345-678-9012'}
students_telephone.update({"Bob": "456-789-0123", "Eva": "567-890-1234"})
print(students_telephone)
# 运行结果: {'Alice': '123-456-0000', 'Bob': '456-789-0123', 'Charlie': '345-678-9012', 'Eva': '567-890-1234'}
