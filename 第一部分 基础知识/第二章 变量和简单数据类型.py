# 变量
message = "Hello Python World！"
print(message)


# 字符串

# title() 方法修改单词首字母为大写
name = "ada lovelace"
print(name.title())

# Ada Lovelace

# upper() 将字符串全部改为大写
# lower() 将字符串全部改为小写
print(name.upper())
print(name.lower())


# 字符串中使用变量
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
# f字符串是python3.6引入的，如果使用的python版本是3.5或更早的版本，需要使用 format()方法
# full_name = "{} {}".format(first_name, last_name)
print(full_name)
print(f"Hello, {full_name.title()}!")


# 制表符
# \t \n

# 删除空白
# rstrip(),用来去除字符串末尾的空格
# lstrip(), 用来去除字符串前面的空格
# strip()，用来去除字符串末尾和前面的空格


# 数
# + - * /
# ** 乘方
# 大一点的数表示方法
universe_age = 14_000_000_000
print(universe_age)

"""
这是因为存储这种数时，Python会忽略其中的下划线。将数字分组时，即便不是将每三
位分成一组，也不会影响最终的值。在Python看来，1000 与1_000 没什么不同，
1_000 与10_00 也没什么不同。这种表示法适用于整数和浮点数，但只有Python 3.6
和更高的版本支持。"""


# 同时给多个变量赋值
x, y, z = 0, 0, 0

# 常量
"""
常量 类似于变量，但其值在程序的整个生命周期内保持不变。Python没有内置的常量类
型，但Python程序员会使用全大写来指出应将某个变量视为常量，其值应始终不变："""
MAX_CONNETCTION = 5000


# 注释
# 这是一条注释
"""
这是一条长注释"""

import this

