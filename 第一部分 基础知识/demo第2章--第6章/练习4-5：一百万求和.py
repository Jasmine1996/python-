"""
练习4-5：一百万求和 　创建一个包含数1～1 000 000的列表，再使用min()
和max() 核实该列表确实是从1开始、到1 000 000结束的。另外，对这个列表
调用函数sum() ，看看Python将一百万个数相加需要多长时间。
"""

num_list = [value for value in range(1, 1000001)]
print(min(num_list))
print(max(num_list))
import time
start_time = time.time()
print(sum(num_list))
# import os
# time.sleep(5)
end_time = time.time()
print(end_time - start_time)
