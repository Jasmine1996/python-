"""
练习9-6：冰激凌小店 　冰激凌小店是一种特殊的餐馆。编写一个名为
IceCreamStand 的类，让它继承为完成练习9-1或练习9-4而编写的
Restaurant 类。这两个版本的Restaurant 类都可以，挑选你更喜欢的那
个即可。添加一个名为flavors 的属性，用于存储一个由各种口味的冰激凌组
成的列表。编写一个显示这些冰激凌的方法。创建一个IceCreamStand 实
例，并调用这个方法。
"""
class Restaurant:
    """一个表示餐馆的类"""
    def __init__(self,restaurant_name, cuisine_type):
        """初始化餐馆。"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """显示餐馆信息摘要。"""
        msg = f"{self.restaurant_name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = f"{self.restaurant_name} is open. Come on in !"
        print(f"\n{msg}")

class IceCreamStand(Restaurant):
    """一个表示冰激凌小店的类。"""
    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        """初始化冰激凌小店。"""

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['酸', '甜', '苦', '辣']
    def describe_ice(self):
        """显示出售的冰激凌品种。"""
        print(f"{self.flavors}")

ice = IceCreamStand("山西面馆","面条")
ice.describe_ice()

