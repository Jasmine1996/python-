"""
练习10-12：记住喜欢的数 　将练习10-11中的程序合二为一。如果存储了用户
喜欢的数，就向用户显示它，否则提示用户输入喜欢的数并将其存储到文件
中。运行这个程序两次，看看它能否像预期的那样工作。
"""
import json
filename = '../dir_demo/like_num.txt'

try:
    with open(filename, 'r') as f:
        lines = f.readlines()

except FileNotFoundError:
    num = input("提示用户输入喜欢的数")
    with open(filename, 'w') as f:
        json.dump(num, f)
# else:
#     for line in lines:
#         print(f"I know your favorite number! It's {line.rstrip()}.")
