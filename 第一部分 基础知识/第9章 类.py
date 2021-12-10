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
    def __init__(self, make, model, year):
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
# a.直接修改属性的值
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# b.通过方法修改属性的值
"""
可对方法update_odometer() 进行扩展，使其在修改里程表读数时做些额外
的工作。下面来添加一些逻辑，禁止任何人将里程表读数往回调：
"""

class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self, make, model, year):
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

    def update_odometer(self,mileage):
        """將里程表读数设置为指定的值。
        禁止将里程表读数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(2.3)
my_new_car.read_odometer()


# c. 通过方法对属性的值进行递增
"""
有时候需要将属性值递增特定的量，而不是将其设置为全新的值。假设我们购
买了一辆二手车，且从购买到登记期间增加了100英里的里程。下面的方法让我
们能够传递这个增量，并相应地增大里程表读数："""

class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 500
    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车历程的信息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """將里程表读数设置为指定的值。
        禁止将里程表读数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles
my_used_car = Car('subaru','outback',2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


