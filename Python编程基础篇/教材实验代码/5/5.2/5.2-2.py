class Lion(object):
    # 定义狮子的名字和年龄
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 定义狮子发出响声的方法
    def make_sound(self):
        print(self.name + "发出声音")
lion = Lion("舒克",3)
print(lion.name)        # 输出: 舒克
print(lion.age)         # 输出: 3
lion.make_sound()       # 输出: 舒克发出声音
Lion.height=1           # 通过类名.属性，动态添加类属性
print(Lion.height)      # 输出结果为 1

lion = Lion("贝塔",4)
lion.height=1           # 通过实例对象.属性，动态添加实例属性
print(lion.height)      # 输出结果为 1
