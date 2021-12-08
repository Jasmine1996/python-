"""
练习3-5：修改嘉宾名单 　你刚得知有位嘉宾无法赴约，因此需要另外邀请一
位嘉宾。
以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，
指出哪位嘉宾无法赴约。
修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
再次打印一系列消息，向名单中的每位嘉宾发出邀请。"""

people = ["jasmine", 'lisa', 'tom']
print(people)
msg = f"hello {people[0]},welcome to my party"
print(msg)

did_not = 'tom'
people.remove(did_not)
print(people, did_not ,"is did't come")
did_replace = 'kali'
people.append(did_replace)
print(people)
msg = f"hello {people[0]},welcome to my party"
print(msg)