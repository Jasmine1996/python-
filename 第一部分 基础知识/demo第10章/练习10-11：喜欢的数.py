"""
练习10-11：喜欢的数 　编写一个程序，提示用户输入喜欢的数，并使用
json.dump() 将这个数存储到文件中。再编写一个程序，从文件中读取这个
值，并打印如下所示的消息。
I know your favorite number! It's _____.
"""
import json
filename = '../dir_demo/like_num.txt'
num = input("提示用户输入喜欢的数")
with open(filename, 'w') as f:
    json.dump(num, f)
    # print(f"I know your favorite number! It's {num}.")
with open(filename, 'r') as f:
    for line in f:
        print(f"I know your favorite number! It's {line}.")