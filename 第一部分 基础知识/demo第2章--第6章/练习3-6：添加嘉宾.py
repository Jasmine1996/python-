"""
练习3-6：添加嘉宾 　你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想
想你还想邀请哪三位嘉宾。
以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条
print 语句，指出你找到了一个更大的餐桌。
使用insert() 将一位新嘉宾添加到名单开头。
使用insert() 将另一位新嘉宾添加到名单中间。
使用append() 将最后一位新嘉宾添加到名单末尾。
打印一系列消息，向名单中的每位嘉宾发出邀请。
"""
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
begin = 'a'
center = 'b'
last = 'c'
people.insert(0, begin)
people.insert(2, center)
people.append(last)
print(people)