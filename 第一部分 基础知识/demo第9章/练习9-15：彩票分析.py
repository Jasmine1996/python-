"""
练习9-15：彩票分析 　可以使用一个循环来明白前述彩票大奖有多难中奖。为
此，创建一个名为my_ticket 的列表或元组，再编写一个循环，不断地随机
选择数或字母，直到中大奖为止。请打印一条消息，报告执行循环多少次才中
了大奖。
"""

my_ticket = (1,2,3,4)
from random import choice
tuple_ = (1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e')
list_ = []

# for _ in range(4):

falg = False
num = 0

while not falg:
    while len(list_) < 4:
        tmp = choice(tuple_)
        if tmp not in list_:
            list_.append(tmp)

    if list_ == my_ticket:
        flag = True
    else:
        list_ = []
    num += 1
print(f"while循环了 {num}次，猜对了 {my_ticket}")