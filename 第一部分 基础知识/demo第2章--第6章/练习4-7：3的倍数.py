"""
练习4-7：3的倍数 　创建一个列表，其中包含3～30能被3整除的数，再使用一
个for 循环将这个列表中的数打印出来。
"""
num_3 = [value for value in range(3, 31, 3)]
print(num_3)
for num in num_3:
    print(num)