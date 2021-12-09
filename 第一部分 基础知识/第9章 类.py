# 9 类

# 9.1 创建和使用类
# 9.1.1 创建Dog 类
# dog.py
class Dog:
    """一次模拟小狗的简单尝试。"""

    def __init__(self,name,age):
        """初始化属性 name和 age。"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")

# 9.1.2 根据类创建实例
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

# 使用类和实例
# 9.2.1 Car类
# car.py
class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

# 9.2.2 给属性指定默认值
class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车历程的信息。"""
        print(f"This car has {self.odometer_reading} miles on it.")
my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# 9.2.3 修改属性的值
