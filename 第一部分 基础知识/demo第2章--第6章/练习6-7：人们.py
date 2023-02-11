"""
练习6-7：人们 　在为完成练习6-1而编写的程序中，再创建两个表示人的字
典，然后将这三个字典都存储在一个名为people 的列表中。遍历这个列表，
将其中每个人的所有信息都打印出来。
"""

person_0 = {
    'first': '彭',
    'last': '飞',
    'age': 27,
    'city': 'shenzhen',
}

person_1 = {
    'first': '杨',
    'last': '恒',
    'age': 27,
    'city': 'beijing',
}

person_2 = {
    'first': '武',
    'last': '雷震',
    'age': 28,
    'city': '杭州',
}
people = [person_0, person_1, person_2]
for person in people:
    # for k, v in person.items():
    print(f"\nFullName: {person['first']}{person['last']}")
    print(f"\tage: {person['age']}\n\tcity: {person['city']}")