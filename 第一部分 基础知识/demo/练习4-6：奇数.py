"""
练习4-6：奇数 　通过给函数range() 指定第三个参数来创建一个列表，其中
包含1～20的奇数，再使用一个for 循环将这些数打印出来。
"""
odd_nums = [value for value in range(1, 20, 2)]
print(odd_nums)
for odd in odd_nums:
    print(odd)