"""
练习9-4：就餐人数 　在为完成练习9-1而编写的程序中，添加一个名为
number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为
restaurant 的实例。打印有多少人在这家餐馆就餐过，然后修改这个值并再
次打印它。

添加一个名为set_number_served() 的方法，让你能够设置就餐人数。调
用这个方法并向它传递一个值，然后再次打印这个值。

添加一个名为increment_number_served() 的方法，让你能够将就餐人数
递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待
的就餐人数。
"""

class Restaurant:
    """一个表示餐馆的类"""
    def __init__(self,restaurant_name, cuisine_type):
        """初始化餐馆。"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def set_number_served(self,num):
        """能够设置就餐人数"""
        self.number_served = num

    def increment_number_served(self, num):
        """让你能够将就餐人数
递增。调用这个方法并向它传递一个这样的值"""
        self.number_served += num
    def describe_restaurant(self):
        """显示餐馆信息摘要。"""
        msg = f"{self.restaurant_name} serves wonderful {self.cuisine_type}, 可以容纳{self.number_served}"
        print(f"\n{msg}")

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = f"{self.restaurant_name} is open. Come on in !"
        print(f"\n{msg}")

r1 = Restaurant("山西面馆", "面条")
r1.describe_restaurant()

r1.set_number_served(5)
r1.describe_restaurant()

r1.increment_number_served(10)
r1.describe_restaurant()