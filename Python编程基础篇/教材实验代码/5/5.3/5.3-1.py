class Animal:
    def __init__(self, name, age):
        self.__name = name   # 变形为 self._Animal__name
        self.__age = age     # 自动变形为 self._Animal__age
lion = Animal("狮子", 5)
print(lion.__dict__)        # __dict__ 查看对象内部所有属性字典
lion.__sound = "狮吼"       # 动态新增 __sound 属性
print(lion.__dict__)
