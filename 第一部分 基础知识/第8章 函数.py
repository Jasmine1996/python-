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
