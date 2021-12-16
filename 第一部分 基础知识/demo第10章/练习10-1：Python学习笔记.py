"""
练习10-1：Python学习笔记 　在文本编辑器中新建一个文件，写几句话来总结
一下你至此学到的Python知识，其中每一行都以“In Python you can”打头。
将这个文件命名为learning_python.txt，并存储到为完成本章练习而编写的程
序所在的目录中。编写一个程序，它读取这个文件，并将你所写的内容打印三
次：第一次打印时读取整个文件；第二次打印时遍历文件对象；第三次打印时
将各行存储在一个列表中，再在with 代码块外打印它们。
"""

print("---Reading in entire file:")
filename = './learning_python.txt'
with open(filename, 'r') as f:
    contents = f.read()

print(contents)

print("\n--- Looping over the lines:")
with open(filename, 'r') as f:
    for line in f:
        print(line)

print("\n Storing the lines in a list:")
with open(filename) as f:
    # lines = f.readlines()
    lines = f.read()
for line in lines:
    print(line.rstrip())