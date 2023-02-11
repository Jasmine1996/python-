"""
练习4-11：你的比萨，我的比萨 　在你为完成练习4-1而编写的程序中，创建
比萨列表的副本，并将其赋给变量friend_pizzas ，再完成如下任务。
在原来的比萨列表中添加一种比萨。
在列表friend_pizzas 中添加另一种比萨。
核实有两个不同的列表。为此，打印消息“My favorite pizzas are:”，
再使用一个for 循环来打印第一个列表；打印消息“My friend's
favorite pizzas are:”，再使用一个for 循环来打印第二个列表。核实
新增的比萨被添加到了正确的列表中。
"""
pizzas = ['乐凯撒', '尊宝披萨', '至尊披萨']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")
print(f"I really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append('必胜客')
friend_pizzas.append('不知名品牌')

print(f"My favorite pizzas are: {pizzas}")
print(f"My friend's favorite pizzas are: {friend_pizzas}")

