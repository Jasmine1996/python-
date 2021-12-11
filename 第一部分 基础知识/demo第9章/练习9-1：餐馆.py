"""
练习9-1：餐馆 　创建一个名为Restaurant 的类，为其方法__init__()
设置属性restaurant_name 和cuisine_type 。创建一个名为
describe_restaurant() 的方法和一个名为open_restaurant() 的方
法，前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用
前述两个方法。
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

restaurant = Restaurant("the mean queen", 'pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()