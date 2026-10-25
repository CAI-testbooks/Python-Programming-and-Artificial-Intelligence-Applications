class Animal:
    def speak(self):
        return "动物发出声音"

class Dog(Animal):
    def speak(self):
        return "汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵"

def make_sound(animal):
    print(animal.speak())

make_sound(Animal())  # 输出：动物发出声音
make_sound(Dog())     # 输出：汪汪
make_sound(Cat())     # 输出：喵喵
