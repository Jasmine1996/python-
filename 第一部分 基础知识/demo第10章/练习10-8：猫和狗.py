"""
练习10-8：猫和狗 　创建文件cats.txt和dogs.txt，在第一个文件中至少存储
三只猫的名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试
读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except
代码块中，以便在文件不存在时捕获FileNotFound 错误，并显示一条友好的
消息。将任意一个文件移到另一个地方，并确认except 代码块中的代码将正
确执行。
"""

filename_cat = '../dir_demo/cats.txt'
filename_dog = '../dir_demo/dogs.txt'
with open(filename_dog, 'w') as f:
    f.write("dog1\ndog2\ndog3 \n")
with open(filename_cat, 'w') as f:
    f.write("cat1\ncat2\ncat3\n")

try:
    with open(filename_cat, 'r') as f:
        for line in f:
            print(line.rstrip())
    with open(filename_dog, 'r') as f:
        for line in f:
            print(line.rstrip())
except FileNotFoundError:
    print(f"请检查文件是否存在{filename_dog} {filename_cat}")