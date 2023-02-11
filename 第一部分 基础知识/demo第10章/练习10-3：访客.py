"""
练习10-3：访客 　编写一个程序，提示用户输入名字。用户做出响应后，将其
名字写入文件guest.txt中。
"""
filename = '../dir_demo/访客.txt'

while True:
    username = input("用户输入名字（用户名存在../dir_demo/访客.txt，如需退出请输入q）: ")
    if username.lower() == 'q':
        break
    with open(filename, 'a') as f:
        f.write(username + "\n")

