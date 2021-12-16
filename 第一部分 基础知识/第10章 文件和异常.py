# 10.1 从文件中读取数据
"""
要使用文本文件中的信息，首先需要将信息读取到内存中。为此，你可以一次性读
取文件的全部内容，也可以以每次一行的方式逐步读取。
"""

# 10.1.1 读取整个文件
# file_reader.py
with open('./dir_demo/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print("-"*30)
print(contents.lstrip())

# 10.1.2 文件路径

# 10.1.3 逐行读取
# file_reader.y
filename = './dir_demo/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 10.1.4 创建一个包含文件各行内容的列表
filename = './dir_demo/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 10.1.5 使用文件的内容
# pi_string.py
filename = './dir_demo/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


# 10.1.6 包含一百万位的大型文件
# pi_string.py
filename = './dir_demo/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:20]}...")
print(len(pi_string))


# 10.1.7 圆周率值中包含你的生日吗

birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first millino digits of pi!")
else:
    print("Your birthday does not appear in the dirst nillon digits of pi.")

# 10.2 写入文件
# 10.2.1 写入空文件
# write_message.py
filename = './dir_demo/programming.txt'
# 可指定读取模式 （'r' ）、写入模式 （'w' ）、
# 附加模式 （'a' ）或读 写模式 （'r+' ）。
# 如果省略了模式实参，Python将以默认的只读模式打开文件。
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")


# 10.2.2 写入多行
# 函数write() 不会在写入的文本末尾添加换行符，因此如果写入多行时没有指定换
# 行符，文件看起来可能不是你希望的那样：
filename = './dir_demo/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
# 要让每个字符串都单独占一行，需要在方法调用write() 中包含换行符：
    file_object.write("\nI love programming.\n")
    file_object.write("I love creating new games.\n")

# 10.2.3 附加到文件（>> 追加）
# write_message.py
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# 10.3 异常
"""
Python使用称为异常 的特殊对象来管理程序执行期间发生的错误。每当发生让
Python不知所措的错误时，它都会创建一个异常对象。如果你编写了处理该异常的
代码，程序将继续运行；如果未对异常进行处理，程序将停止并显示traceback，其
中包含有关异常的报告。"""

# 10.3.1 处理 ZeroDivisionError 异常
# division_calculator.py
# print(5/0)

# 10.3.2 使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# 10.3.3 使用异常避免崩溃
# division_calculator.py
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
# 10.3.4 else 代码块
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


# 10.3.5 处理FileNotFoundError 异常
# alice.py
filename = 'dir_demo/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry,the file {filename} does not exist! ")

# 10.3.6 分析文本
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry,the file {filename} does not exist.")
else:
    # 计算该文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")



# 10.3.7 使用多个文件( 函数版本
def count_words(filename):
    """计算一个文件大致包含多少个单词。"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} ones not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['dir_demo/pi_digits.txt','test1','test2','test3']
for filename in filenames:
    count_words(filename)


# 10.3.8 静默失败
# pass 关键字

# 10.3.9 决定报告那些错误



# 10.4 存储数据
"""
很多程序都要求用户输入某种信息，如让用户存储游戏首选项或提供要可视化的数
据。不管关注点是什么，程序都把用户提供的信息存储在列表和字典等数据结构
中。用户关闭程序时，几乎总是要保存他们提供的信息。一种简单的方式是使用模
块json 来存储数据。
模块json 让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时
加载该文件中的数据。你还可以使用json 在Python程序之间分享数据。更重要的
是，JSON数据格式并非Python专用的，这让你能够将以JSON格式存储的数据与使用
其他编程语言的人分享。这是一种轻便而有用的格式，也易于学习。
注意 　JSON（JavaScript Object Notation）格式最初是为JavaScript开发
的，但随后成了一种常见格式，被包括Python在内的众多语言采用。
"""

# 10.4.1 使用json.dump()和json.load()
# 函数json.dump() 接受两个实参：要存储的数据，以及可用于存储数据的文件对
# 象。

# numbe_writer.py
import json
numbers = [2,3,5,7,11,13]

filename = 'dir_demo/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)


# 下面再编写一个程序，使用json.load() 将列表读取到内存中：
# 这是一种在程序之间共享数据的简单方式。
import json
filename = 'dir_demo/numbers.json'
with open(filename,'r') as f:
    numbers = json.load(f)

print(numbers)

# 10.4.2 保存和读取用户生成的数据
"""
使用json 保存用户生成的数据大有裨益，因为如果不以某种方式存储，用户的信
息会在程序停止运行时丢失。下面来看一个这样的例子：提示用户首次运行程序时
输入自己的名字，并在再次运行程序时记住他。
"""
# remember_me.py
import json
username = input("what is your name?")

filename = 'dir_demo/username.json'
with open(filename,'w') as f:
    json.dump(username,f)
    print(f"we'll remember you when you come back,{username}!")

# greet_user.py
with open(filename, 'r') as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")




# 合并到一个程序
import json
# 如果以前存储了用户名，就加载他
# 否则，提示用户输入用户名并存储它
filename = 'dir_demo/username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("what is your name? ")
    with open(filename, 'w') as f:
        json.dump(username,f)
        print(f"we'll remember you when you come back,{username}!")

else:
    print(f"Welcome back,{username}")


# 10.4.3 重构
# 需要好好练习这里