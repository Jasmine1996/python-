"""
练习3-7：缩减名单 　你刚得知新购买的餐桌无法及时送达，因此只能邀请两
位嘉宾。
以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条
你只能邀请两位嘉宾共进晚餐的消息。
使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名
单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀
请他来共进晚餐。
对于余下两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之
列。
使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，
核实程序结束时名单确实是空的。
"""

people = ["jasmine", 'lisa', 'tom']
print(people)
msg = f"hello {people[0]},welcome to my party"
print(msg)

did_not = 'tom'
people.remove(did_not)
print(people, did_not , "is did't come")
did_replace = 'kali'
people.append(did_replace)
print(people)
msg = f"hello {people[0]},welcome to my party"
print(msg)
begin = 'a'
center = 'b'
last = 'c'
people.insert(0, begin)
people.insert(2, center)
people.append(last)
print(people)

while len(people) > 2:
    popped_people = people.pop()
    msg = f"sorry {popped_people.title()}, 不能邀请您共进晚餐了。"
    print(msg)
print(people)
print(f"hello {people[0].title()},您还在名单内")
print(f"hello {people[1].title()},您还在名单内")

