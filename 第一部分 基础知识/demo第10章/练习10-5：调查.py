"""
练习10-5：调查 　编写一个while 循环，询问用户为何喜欢编程。每当用户
输入一个原因后，都将其添加到一个存储所有原因的文件中。
"""

filename = '../dir_demo/code_why.txt'

while True:
    msg = input("询问用户为何喜欢编程，请输入(如没有输入，请按q退出，不区分大小写):")
    if msg.lower() == 'q':
        break
    with open(filename, 'a') as f:
        f.write(f"{msg}\n")