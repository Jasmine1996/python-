"""
练习10-4：访客名单 　编写一个while 循环，提示用户输入名字。用户输入
名字后，在屏幕上打印一句问候语，并将一条到访记录添加到文件
guest_book.txt中。确保这个文件中的每条记录都独占一行。
"""

filename = '../dir_demo/guest_book.txt'
while True:
    username = input("用户输入名字（用户名存在../dir_demo/访客.txt，如需退出请输入q）: ")
    if username.lower() == 'q':
        break
    with open(filename, 'a') as f:
        f.write(f"Welcome to here,{username.title()}\n")