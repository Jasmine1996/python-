# 6.1 一个简单地字典

# alien.py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


# 6.2 使用字典

# 6.2.2 添加键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_positino'] = 25
print(alien_0)

# 6.2.3 先创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


# 6.2.4 修改字典中的值
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

"""
对一个能够以不同速度移动的外星人进行位置跟踪。为
此，我们将存储该外星人的当前速度，并据此确定该外星人将向右移动多远：
"""
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快。
    x_increment = 3

# 新位置为旧位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")



# 6.2.5 删除键值对
# alien.py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['color']
print(alien_0)
# 注意： 删除的键值对会永远消失

# 6.2.6 由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")


# 6.2.7 使用get() 来访问值
# alien_no_points.py
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])
# error : KeyError: 'points'

# 第10章 会介绍如何处理类似的错误
# 但对字典而言，可以使用get() 方法在指定的键不存在是返回一个默认值，从而避免这样的错误
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# 6.3 遍历字典
# 6.3.1 遍历所有键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print((f"\nValue: {value}"))

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")



# 遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())



friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}")


if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll')


# 6.3.3 按特定顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# 6.3.4 遍历字典中所有的值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# set() 集合，剔除重复项
print("user set() after")
for language in set(favorite_languages.values()):
    print(language.title())


# 6.4 嵌套
"""
有时候，需要将一系列字典存储在列表中，或将列表作为只存储在字典中
，这称为嵌套
"""

# 6.4.1 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


"""
更符合现实的情形是，外星人不止三个，且每个外星人都是使用代码自动生成的。
在下面的示例中，使用range() 生成了30个外星人："""

# 创建一个用于存储外星人的空列表。
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien_0)

print("...")

# 显示创建了多少个外星人
print((f"Total number of aliens: {len(aliens)}"))

# 要将前三个外星人修改为黄色、速度为中等且值10分，可这
# 样做
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("."*30)


# 6.4.2 在字典中存储列表

# pizza.py
# 存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# 概述所点的披萨
print(f"You ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)


# 一个人可以喜欢多种语言
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is {languages}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")

# 6.4.3 在字典中存储字典
"""
可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。例如，如果有多个网
站用户，每个都有独特的用户名，可在字典中将用户名作为键，然后将每位用户的
信息存储在一个字典中，并将该字典作为与用户名相关联的值。在下面的程序中，
存储了每位用户的三项信息：名、姓和居住地。为访问这些信息，我们遍历所有的
用户名，并访问与每个用户名相关联的信息字典
"""
# many_users.py
users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull_name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


