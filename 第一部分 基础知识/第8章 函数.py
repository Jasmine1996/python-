# 8. 函数
"""
函数是带名字的代码块，用于
完成具体的工作。要执行函数定义的特定任务，可调用 该函数。需要在程序中
多次执行同一项任务时，无须反复编写完成该任务的代码，只需要调用执行该
任务的函数，让Python运行其中的代码即可。你将发现，通过使用函数，程序
编写、阅读、测试和修复起来都更加容易
"""

"""
你还将学习向函数传递信息的方式；学习如何编写主要任务是显示信息的函
数，以及旨在处理数据并返回一个或一组值的函数；最后，学习如何将函数存
储在称为模块 的独立文件中，让主程序文件的组织更为有序。
"""

# 8.1 定义函数

# def 关键字来定义一个函数，函数定义
# greet_user() 函数名
# 最后，定义以冒号结尾

# greeter.py
def greet_user():
    """显示简单的问候语。"""
    print("Hello!")
# 紧跟在def greet_user(): 后面的所有缩进行构成了函数体。
# 文本是称为 文档字符串 （docstring）的注释，描述了函数是做什么的。
# 文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档。

# 調用函数
greet_user()

# 8.1.1 向函数传递信息
def greet_user(username):
    """显示简单的问候语。"""
    print(f"Hello,{username.title()}!")

greet_user('jasmine')

# 8.1.2 实参和形参
"""
在函数greet_user() 的定义中，变量username 是一个形参 （parameter），
即函数完成工作所需的信息。在代码greet_user('jesse') 中，值'jesse' 是
一个实参 （argument），即调用函数时传递给函数的信息。调用函数时，将要让函
数使用的信息放在圆括号内。在greet_user('jesse') 中，将实参'jesse' 传
递给了函数greet_user() ，这个值被赋给了形参username 。 注意 　大家有时候会形参、实参不分，因此如果你看到有人将函数定义中的变
量称为实参或将函数调用中的变量称为形参，不要大惊小怪。
"""

# 8.2 传递实参
# 包含位置实参，关键字实参

# 8.1 位置实参
# pets.py
def describe_pet(animal_type, pet_name):
    """显示宠物信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# 函数可以多次调用
# 位置实参的顺序很重要

# 8.2.2 关键字实参
describe_pet(animal_type='hamster',pet_name='harry')


# 8.2.3 默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

describe_pet('willie')

# 8.2.4 等效的函数调用
# 一条名为Willie的小狗。
describe_pet('willie')
describe_pet(pet_name='willie')

# 一只名为Harry的仓鼠。
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# 8.2.5 避免实参错误
def describe_pet(animal_type,pet_name):
    """显示宠物信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet()


# 8.3 返回值
"""
函数并非总是直接显示输出，它还可以处理一些数据，并返回一个或一组值。函数
返回的值称为返回值 。在函数中，可使用return 语句将值返回到调用函数的代码
行。返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程
序。
"""
# 8.3.1 返回简单值
# formatted_name.py
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 8.3.2 让实参变成可选的
def get_formatted_name(first_name,middle_name,last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# 将中间名改为一个空的默认值
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


# 8.3.3 返回字典
# person.py
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix',age=27)
print(musician)

# 8.3.4 结合函数使用while循环
# greeter.py
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("enter 'q' at any time to quit")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello,{formatted_name}")


# 8.4 传递列表
"""
你经常会发现，向函数传递列表很有用，其中包含的可能是名字、数或更复杂的对
象（如字典）。将列表传递给函数后，函数就能直接访问其内容。下面使用函数来
提高处理列表的效率。"""

"""
假设有一个用户列表，我们要问候其中的每位用户。下面的示例将包含名字的列表
传递给一个名为greet_users() 的函数，这个函数问候列表中的每个人：
greet_users.py"""
def greet_users(names):
    """向列表中的每位用户发出简单的问候。"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hanah', 'ty', 'margot']
greet_users(usernames)

# 8.4.1 在函数中修改列表
"""
来看一家为用户提交的设计制作3D打印模型的公司。需要打印的设计存储在一个列
表中，打印后将移到另一个列表中。下面是在不使用函数的情况下模拟这个过程的
代码："""
# printing_models.py
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['phone case', 'reboot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# 函数版本
def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，知道没有未打印的设计为止。
    打印每个设计后，都将其移到列表completed_models中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'reboot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

"""
该程序还演示了这样一种理念：每个函数都应只负责一项具体的工作。第一个函数
打印每个设计，第二个显示打印好的模型。这优于使用一个函数来完成这两项工
作。编写函数时，如果发现它执行的任务太多，请尝试将这些代码划分到两个函数
中。别忘了，总是可以在一个函数中调用另一个函数，这有助于将复杂的任务划分
成一系列步骤。"""

# 8.4.2 禁止函数修改列表
# function_name(list_name[:])


# 8.5 传递任意数量的实参
# pizza.py
def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
"""
形参名*toppings 中的星号让Python创建一个名为toppings 的空元组，并将收
到的所有值都封装到这个元组中。函数体内的函数调用print() 通过生成输出，证
明Python能够处理使用一个值来调用函数的情形，也能处理使用三个值来调用函数
的情形。它以类似的方式处理不同的调用。注意，Python将实参封装到一个元组
中，即便函数只收到一个值："""

def make_pizza(*toppings):
    """概述要制作的披萨。"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 8.5.1 结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.5.2 使用任意数量的关键字实参
# user_profile.py
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location ='princeton',
                             field='physics')
print(user_profile)


# 8.6 将函数存储在模块中
"""
使用函数的优点之一是可将代码块与主程序分离。通过给函数指定描述性名称，可
让主程序容易理解得多。你还可以更进一步，将函数存储在称为模块 的独立文件
中，再将模块导入 到主程序中。import 语句允许在当前运行的程序文件中使用模
块中的代码。
通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层
逻辑上。这还能让你在众多不同的程序中重用函数。将函数存储在独立文件中后，
可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其
他程序员编写的函数库。"""

def make_pizza(size, *toppings):
    """概述要制作的披萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for toppings in toppings:
        print(f"- {toppings}")


# making_pizzas.py
import pizza
pizza.makepizza(16,'pepperoni')
pizza.makepizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入特定的函数
# from module_name import function_name
# from module_name import function_0,function_1,..

# 8.6.3 使用as 给函数指定别名
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.4 使用 as给模块指定别名
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroomsm')

"""
这样不仅代码更简洁，还让你不用再关注模块名，只专
注于描述性的函数名。这些函数名明确指出了函数的功能，对于理解代码而言，比
模块名更重要"""

# 8.6.5 导入模块中的所有函数
from pizza import *

# 8.7 函数编写指南
"""
给形参指定默认值时，等号两边不要有空格：
def function_name(parameter_0, parameter_1='default value')
对于函数调用中的关键字实参，也应遵循这种约定：
function_name(value_0, parameter_1='value')
"""