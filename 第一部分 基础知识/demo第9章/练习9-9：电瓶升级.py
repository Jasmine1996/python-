"""
练习9-9：电瓶升级 　在本节最后一个electric_car.py版本中，给Battery
类添加一个名为upgrade_battery() 的方法。该方法检查电瓶容量，如果不
是100，就将其设置为100。创建一辆电瓶容量为默认值的电动汽车，调用方法
get_range() ，然后对电瓶进行升级，并再次调用get_range() 。你将看
到这辆汽车的续航里程增加了。
"""
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odmeter(self, miles):
        self.odometer_reading += miles


# 9.3.2 给子类定义属性和方法
class ElectricCar(Car):
    """电动汽车的独特之处。"""
    def __init__(self, make, model, year):
        """初始化父类的属性。"""
        """再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f"The is car has a {self.battery_size}-kWh battery.")


# 9.3.3 重写父类的方法
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        """该方法检查电瓶容量，如果不
是100，就将其设置为100"""
        if self.battery_size != 100:
            self.battery_size = 100


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla.battery.describe_battery()
print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()