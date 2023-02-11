"""
练习7-3：10的整数倍 　让用户输入一个数，并指出该数是否是10的整数倍。
"""

num = input("请输入一个数，我来指出该数是否是10的整数倍：")
num = int(num)
if not num % 10:
    print(f"{num} 可以被10整除")
else:
    print(f"{num} 不可以被10整除")