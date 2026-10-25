class Animal:
    def make_sound(self):
        print("动物发出声音")

class Dog(Animal):
    def make_sound(self):
        print("汪汪")

class Cat(Animal):
    def make_sound(self):
        print("喵喵")

animal: Animal = Animal()
animal.make_sound()

dog: Animal = Dog()
dog.make_sound()

cat: Animal = Cat()
cat.make_sound()
