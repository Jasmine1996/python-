"""
练习6-1：人 　使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居
住的城市。该字典应包含键first_name 、last_name 、age 和city 。将
存储在该字典中的每项信息都打印出来。
"""

person = {
    'first': '彭',
    'last': '飞',
    'age': 27,
    'city': 'shenzhen',
}
for k, v in person.items():
    print(k, ':', v)