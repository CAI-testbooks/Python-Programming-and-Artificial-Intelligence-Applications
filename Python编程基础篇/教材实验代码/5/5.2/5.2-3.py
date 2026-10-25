class Zoo:
    def __init__(self):
        self.animals = []   # 实例属性：保存动物园里所有动物对象的列表

    def add_animal(self, animal):
        self.animals.append(animal)  # 往列表添加动物实例

    def make_animals_sound(self):
        for animal in self.animals:
            animal.make_sound() # 遍历所有动物，调用每只动物的make_sound方法
