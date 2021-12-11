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
with open(filename,'w') as file_object:
    file_object.write("I love programming.")


# 10.2.2 写入多行

