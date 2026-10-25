class Box():
    """容器类，实现了开门、关门方法"""
    def __init__(self,band):
        self.band = band        # 初始化属性品牌名称

    def open_door(self):
        pass

    def close_door(self):
        pass

class IceBox(Box):
    """冰箱"""
    def __init__(self,band,price):
        super().__init__(self,band) # 使用super()函数，调用父类的构造方法
        self.price = price
    def ice(self):
        """制冷"""
        pass
