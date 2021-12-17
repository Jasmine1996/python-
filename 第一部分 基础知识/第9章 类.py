# 9 类

# 9.1 创建和使用类
# 9.1.1 创建Dog 类
# dog.py
class Dog:
    """一次模拟小狗的简单尝试。"""

    def __init__(self, name, age):
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


# 9.3 继承
"""
编写类时，并非总是要从空白开始。如果要编写的类是另一个现成类的特殊版本，
可使用继承 。一个类继承 另一个类时，将自动获得另一个类的所有属性和方法。
原有的类称为父类 ，而新类称为子类 。子类继承了父类的所有属性和方法，同时
还可以定义自己的属性和方法。"""

# 9.3.1 子类的方法__init__()

# electric_car.py
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
        self.battery_size = 75

    def describe_battery(self):
        print(f"The is car has a {self.battery_size}-kWh battery.")


# 9.3.3 重写父类的方法
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# 9.3.4 将实例用作属性
"""
使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清
单以及文件都越来越长。在这种情况下，可能需要将类的一部分提取出来，作为一
个独立的类。可以将大型类拆分成多个协同工作的小类。
"""

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

class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """初始化父类的属性。
        再初始化电动汽车特有的属性"""
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 9.3.5 模拟实物

"""
模拟较复杂的物件（如电动汽车）时，需要解决一些有趣的问题。续航里程是电瓶
的属性还是汽车的属性呢？如果只描述一辆汽车，将方法get_range() 放在
Battery 类中也许是合适的，但如果要描述一家汽车制造商的整个产品线，也许应
该将方法get_range() 移到ElectricCar 类中。在这种情况下，get_range()
依然根据电瓶容量来确定续航里程，但报告的是一款汽车的续航里程。也可以这样
做：仍将方法get_range() 留在Battery 类中，但向它传递一个参数，如
car_model 。在这种情况下，方法get_range() 将根据电瓶容量和汽车型号报
告续航里程。"""




# 9.4 导入类

# 9.4.1 导入单个类
# from car import Car

# 9.4.2 在一个模块中存储多个类
# from car import ElectricCar

# 9.4.3 从一个模块中导入多个类
# from car import Car, ElectricCar

# 9.4.4 导入整个模块
# import car


# 9.4.5 导入模块中的所有类
# 不推荐此导入方式
# from car import *


# 9.4.6 在一个模块中导入另一个模块
# electric_car.py

# 9.4.7 使用别名
# from electric_car import ElectricCar as EC
# my_tesla = EC('tesla', 'roadster', 2019)

# 9.4.8 自定义工作流程
"""如你所见，在组织大型项目的代码方面，Python提供了很多选项。熟悉所有这些选
项很重要，这样你才能确定哪种项目组织方式是最佳的，并能理解别人开发的项
目。
一开始应让代码结构尽可能简单。先尽可能在一个文件中完成所有的工作，确定一
切都能正确运行后，再将类移到独立的模块中。如果你喜欢模块和文件的交互方
式，可在项目开始时就尝试将类存储到模块中。先找出让你能够编写出可行代码的
方式，再尝试改进代码"""






# 9.5 Python标准库
# 1. randint（）
from random import randint
print(randint(1,6))

# 2. choice()
from random import choice
players = ['charles','martina','florence','eli']
first_up = choice(players)
print(first_up)

"""
注意：
创建与安全相关的应用程序时，请不要使用模块random ，但该模块可以很好地用
于创建众多有趣的项目。"""

# 9.6 类编码风格

"""
类的标准和规范
    类名应采用驼峰命名法 ，即将类名中的每个单词的首字母都大写，而不使用下划
线。实例名和模块名都采用小写格式，并在单词之间加上下划线。
    对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地
描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。每个模块也都应
包含一个文档字符串，对其中的类可用于做什么进行描述。
    可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在
模块中，可使用两个空行来分隔类。
    需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import
语句，再添加一个空行，然后编写导入你自己编写的模块的import 语句。在包含
多条import 语句的程序中，这种做法让人更容易明白程序使用的各个模块都来自
何处
"""