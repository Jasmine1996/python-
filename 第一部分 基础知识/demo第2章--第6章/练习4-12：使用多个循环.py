"""
练习4-12：使用多个循环 　在本节中，为节省篇幅，程序foods.py的每个版本
都没有使用for 循环来打印列表。请选择一个版本的foods.py，在其中编写两
个for 循环，将各个食品列表打印出来。
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\n My friend's favorite foods are:")
print(friend_foods)

for food in my_foods:
    print(food)

print("-"*30)
for friend_food in friend_foods:
    print(friend_food)