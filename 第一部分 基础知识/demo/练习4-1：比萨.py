"""
练习4-1：比萨 　想出至少三种你喜欢的比萨，将其名称存储在一个列表中，
再使用for 循环将每种比萨的名称打印出来。
修改这个for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名
称。对于每种比萨，都显示一行输出，下面是一个例子。
I like pepperoni pizza.
在程序末尾添加一行代码，它不在for 循环中，指出你有多喜欢比萨。输
出应包含针对每种比萨的消息，还有一个总结性句子，下面是一个例子。
I really love pizza!
"""

pizzas = ['乐凯撒', '尊宝披萨', '至尊披萨']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")
print(f"I really love pizza!")