"""
练习4-4：一百万 　创建一个包含数1～1 000 000的列表，再使用一个for 循
环将这些数打印出来。（如果输出的时间太长，按Ctrl + C停止输出或关闭输
出窗口。）
"""

num_list = [value for value in range(1, 1000001)]
print(num_list)
for value in num_list:
    print(value)