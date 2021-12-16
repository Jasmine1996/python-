"""
练习10-7：加法计算器 　将为完成练习10-6而编写的代码放在一个while 循
环中，让用户犯错（输入的是文本而不是数）后能够继续输入数。
"""

while True:
    try:
        # input("加法计算器，如果需要退出，请输入 quit ")
        num_1 = int(input("提示用户输入第 1 个数:"))
        num_2 = int(input("提示用户输入第 2 个数:"))
        num_sum = num_1 + num_2
        print(num_sum)
    except ValueError:
        print("请检查输入格式是否为数字!")