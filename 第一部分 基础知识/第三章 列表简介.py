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

# 修改、添加和删除元素
# 修改列表元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# ['honda', 'yamaha', 'suzuki']
# ['ducati', 'yamaha', 'suzuki']

# 在列表中添加元素
# 在列表末尾添加元素
# append() 元素附加到列表
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha', 'suzuki', 'ducati']

# 创建空列表，一个一个传入
motorcycles = []
motorcycles.append('suzuki')
motorcycles.append('yamaha')
print(motorcycles)

# 在列表中插入元素
# 使用 insert() 方法
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

"""方法insert() 在索
引0 处添加空间，并将值'ducati' 存储到这个地方。这种操作将列表中既有的每
个元素都右移一个位置："""
# ['ducati', 'honda', 'yamaha', 'suzuki']

# 从列表中删除元素
# 01 使用del 语句删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# ['yamaha', 'suzuki']
# 使用del 语句将值从列表中删除后，你就无法再访问它了。

# 02 使用pop() 删除元素
# pop([-1]) 默认不指定索引，就是-1，也可以指定
"""方法pop() 删除列表末尾的元素，并让你能够接着使用它。术语弹出 （pop）源自
这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
下面来从列表motorcycles 中弹出一款摩托车："""

motorcycles = ['honda','yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha']
# suzuki

# pop的实际使用场景，先进后出
last_owner = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owner.title()}.")

"""
pop 和del的区别！！！
如果你不确定该使用del 语句还是pop() 方法，下面是一个简单的判断标准：如果
你要从列表中删除一个元素，且不再以任何方式使用它，就使用del 语句；如果你
要在删除元素后还能继续使用它，就使用方法pop() 。
"""

# 04根据值删除元素
# remove（）
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# ['honda', 'yamaha', 'suzuki', 'ducati']
# ['honda', 'yamaha', 'suzuki']

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")



