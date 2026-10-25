# 定义基类Animal
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self.__health_status = "Healthy"  # 私有属性：健康状态

    def set_health_status(self, status):
        """设置健康状态(封装)"""
        self.__health_status = status

    def get_health_status(self):
        """获取健康状态(封装)"""
        return self.__health_status

    def display_info(self):
        """展示通用信息"""
        print(f"Name: {self.name}, Age: {self.age}, Species: {self.species}")

    def perform(self):
        """默认表演方法，可被子类覆盖"""
        print(f"{self.name} is just relaxing.")

# 定义食肉动物类
class Carnivore(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def perform(self):
        """重写表演方法"""
        print(f"{self.name} roars loudly and shows its sharp teeth!")

# 定义食草动物类
class Herbivore(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def perform(self):
        """重写表演方法"""
        print(f"{self.name} hops around and munches on some grass!")

# 定义管理员类 Elephant
class Elephant:
    def __init__(self):
        self.animal_list = []  # 动物列表

    def add_animal(self, animal):
        """添加动物到乐园"""
        self.animal_list.append(animal)
        print(f"Added {animal.name} to the animal park.")

    def list_animals(self):
        """列出所有动物的信息"""
        print("\nAnimal List")
        for animal in self.animal_list:
            animal.display_info()

# 定义游客类 Squirrel
class Squirrel:
    def __init__(self, name):
        self.name = name

    def arrange_performance(self, animal):
        """安排动物表演"""
        print(f"\n{self.name} says: Let's watch {animal.name}'s performance!")
        animal.perform()

# 测试代码
if __name__ == "__main__":
    # 创建管理员和游客
    elephant_admin = Elephant()
    squirrel_visitor = Squirrel("Sammy")

    # 创建动物
    lion = Carnivore("Leo", 5, "Lion")
    rabbit = Herbivore("Bunny", 2, "Rabbit")

    # 添加动物到乐园
    elephant_admin.add_animal(lion)
    elephant_admin.add_animal(rabbit)

    # 显示动物列表
    elephant_admin.list_animals()

    # 安排表演
    squirrel_visitor.arrange_performance(lion)
    squirrel_visitor.arrange_performance(rabbit)

    # 修改健康状态
    lion.set_health_status("Injured")
    print(f"\n{lion.name}'s health status: {lion.get_health_status()}")
