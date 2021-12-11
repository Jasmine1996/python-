"""
练习9-14：彩票 　创建一个列表或元组，其中包含10个数和5个字母。从这个
列表或元组中随机选择4个数或字母，并打印一条消息，指出只要彩票上是这4
个数或字母，就中大奖了
"""
from random import choice
tuple_ = (1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e')
list_ = []

# for _ in range(4):
while len(list_) < 4:
    tmp = choice(tuple_)
    if tmp not in list_:
        list_.append(tmp)
print(list_)

