# 4.1 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your to see your net trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")


# 4.2 避免缩进错误
# 4.2.2 避免缩进额外的代码行
# 4.2.3 不必要的缩进
# 4.2.4 循环后不必要的缩进

# 4.3 创建数值列表
# 4.3.1 使用函数range(). 前包后不包 [1,5)
for value in range(1, 5):
    print(value)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

"""
使用函数range() 几乎能够创建任何需要的数集。例如，如何创建一个列表，其中
包含前10个整数（1～10）的平方呢？在Python中，用两个星号（** ）表示乘方运
算。下面的代码演示了如何将前10个整数的平方加入一个列表中："""
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# 4.3.3對数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

# 4.3.4 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

# 4.4 使用列表的一部分
# 4.4.1 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])

# ['charles', 'martina', 'michael']
# ['martina', 'michael', 'florence']
# ['charles', 'martina', 'michael', 'florence']

print(players[2:])
# ['michael', 'florence', 'eli']

print(players[-3:])
# ['michael', 'florence', 'eli']

# 4.4.2 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)

# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\n My friend's favorite foods are:")
print(friend_foods)

# 4.5 元组
"""
列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这
对处理网站的用户列表或游戏中的角色列表至关重要。然而，有时候你需要创建一
系列不可修改的元素，元组可以满足这种需求。Python将不能修改的值称为不可变 的 ，而不可变的列表被称为元组 。"""

# 4.5.1 定义元组
# dimensions.py
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

"""
　严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更
清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号：
my_t = (3,)
"""

# 4.5.2  遍历元组中的所有值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# 修改元组变量
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)