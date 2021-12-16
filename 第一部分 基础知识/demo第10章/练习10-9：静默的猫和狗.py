"""
练习10-9：静默的猫和狗 　修改你在练习10-8中编写的except 代码块，让程
序在任意文件不存在时静默失败。
"""

filename_cat = '../dir_demo/cats.txt'
filename_dog = '../dir_demo/dogs.txt'
# with open(filename_dog, 'w') as f:
#     f.write("dog1\ndog2\ndog3 \n")
# with open(filename_cat, 'w') as f:
#     f.write("cat1\ncat2\ncat3\n")

try:
    with open(filename_cat, 'r') as f:
        for line in f:
            print(line.rstrip())
    with open(filename_dog, 'r') as f:
        for line in f:
            print(line.rstrip())
except FileNotFoundError:
    # print(f"请检查文件是否存在{filename_dog} {filename_cat}")
    pass