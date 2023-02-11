# 5.1 一个简单示例
# cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# 5.2 条件测试
# 5.2.1 检查是否相等
# ==

# 5.2.2 检查是否相等时忽略大小写
car.lower() == 'audi'

# 5.2.3 检查是否不相等
# !=

# 5.2.4 数值比较
# = != >= <= > <

# 5.2.5 检查多个条件
# a。使用and 检查多个条件
# age_0 >= 21 and age_1 >= 21
# (age_0 >= 21) and (age_1 >= 21)

# b。 使用or检查多个条件
# age_0 >= 21 or age_1 >= 21

# 5.2.6 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

# True
# False

# 5.2.7 检查特定值是否不包含在列表中
# not in

# banned_users.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish")

# 5.2.8 布尔表达式
game_active = True
can_edit = False

# 5.3 if 语句
# 5.3.1 简单的if 语句

# voting.py
age =19
if age >= 18:
    print("you are old enough to vote")


# 5.3.2 if-else语句
age = 17
if age >= 18:
    print("you are old enough to vote")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# 5.3.3 if-elif-else
"""
4岁以下免费；
4～18岁收费25美元；
18岁（含）以上收费40美元。
"""

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")



# 5.4 使用if 语句处理列表
# 5.4.1 检查特殊元素
# for循环中嵌套 if判断

# 5.4.2 确定列表不是空的
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


# 5.4.3 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\n Finished making your pizza!")

# 5.5 設置if语句的格式
# 运算符前后加空格
