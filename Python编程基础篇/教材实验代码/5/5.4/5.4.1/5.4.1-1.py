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

    def ice(self):
        """制冷"""
        pass

class WaterBox(Box):
    """洗衣机"""

    def add_water(self):
        """加水"""
        pass

    def sub_water(self):
        """排水"""
        pass

    def wash(self):
        """洗涤"""
        pass
