"""
练习4-10：切片 　选择你在本章编写的一个程序，在末尾添加几行代码，以完
成如下任务。
打印消息“The first three items in the list are:”，再使用切片来
打印列表的前三个元素。
打印消息“Three items from the middle of the list are:”，再使用
切片来打印列表的中间三个元素。
打印消息“The last three items in the list are:”，再使用切片来打
印列表的末尾三个元素。
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three items in the list are:",players[:3])
half = len(players)/2
print(half)
print("Three items from the middle of the list are:",players[1:-1])
print("The last three items in the list are:", players[-3:])
