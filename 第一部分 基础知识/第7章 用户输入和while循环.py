# # 函数input（）的工作原理
# message = input("Tell me something, and I willrepeat it back to you:")
# print(message)
#
#
# # greeter.py
# name = input("Please enter your name:")
# print(f"\nHello,{name.title()}!")
#
# # 7.1.2 使用int（） 来获取数值输入
# age = input("How old are you?")
# age = int(age)
# if age >=18:
#     print(True)
# elif age <40:
#     print(False)
# else:
#     print(None)
#
#
# # rollercoaster.py
# height = input("How tall are you, in inches?")
# height = int(height)
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")
#
#
# # 7.1.3 求模运算符
# # >>> 4%3
# # 1
# # >>> 5%3
# # 2
# # >>> 6%3
# # 0
# # >>> 7*3
# # 21
# # >>> 7%3
# # 1
#
# # even_or_add.py
# number = input("Enter a number,and I'll tell you if it's even or odd:")
# number = int(number)
#
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")
#
# # 7.2 while 循环简介
# # 7.2.1 使用while循环
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
# # 7.2.2 让用户选择何时退出
# prompt = "\n Tell me something,and I will repeat it back to you:"
# prompt +="\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# # 7.2.3 使用标志 flag
# """
# 在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序
# 是否处于活动状态。这个变量称为标志 （flag），充当程序的交通信号灯。可以让
# 程序在标志为True 时继续运行，并在任何事件导致标志的值为False 时让程序停
# 止运行。这样，在while 语句中就只需检查一个条件：标志的当前值是否为True
# 。然后将所有其他测试（是否发生了应将标志设置为False 的事件）都放在其他地
# 方，从而让程序更整洁。
# """
#
# prompt = "\n Tell me something,and I will repeat it back to you:"
# prompt +="\nEnter 'quit' to end the program."
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
#

# # 7.2.4 使用break 退出循环
# # cities.py
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# 7.2.5 在循环中使用continue
# counting.py
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


# 7.2.6 避免无限循环
# counting.py
x = 1
while x <= 5:
    print(x)
    x += 1

#7.3.1 在列表之间移动元素
# confirmed_users.py
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []


# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的用户都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())



# 7.3.2 删除为特定值的所有列表元素
# pets.py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# 7.3.3 使用用户输入来填充字典
# mountain_poll.py
responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")

    # 将回答存储在字典中
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")



