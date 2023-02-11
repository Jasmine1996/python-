"""
练习9-2：三家餐馆 　根据为完成练习9-1而编写的类创建三个实例，并对每个
实例调用方法describe_restaurant() 。
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

mean_queen = Restaurant("the mean queen", "pizza")
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()