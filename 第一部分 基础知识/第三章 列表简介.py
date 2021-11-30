# 列表
"""
概念：
列表 由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0
～9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没
有任何关系。列表通常包含多个元素，因此给列表指定一个表示复数的名称（如
letters 、digits 或names ）是个不错的主意。
在Python中，用方括号（[] ）表示列表，并用逗号分隔其中的元素。下面是一个简单的
列表示例，其中包含几种自行车：
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表元素
print(bicycles[0])
print(bicycles[0].title())

# 索引
print(bicycles[-1])

# 使用列表中的各个值
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

