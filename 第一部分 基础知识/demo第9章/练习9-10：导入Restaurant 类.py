"""
练习9-10：导入Restaurant 类 　将最新的Restaurant 类存储在一个模块
中。在另一个文件中，导入Restaurant 类，创建一个Restaurant 实例并
调用Restaurant 的一个方法，以确认import 语句正确无误。
"""

from restaurant import Restaurant
r = Restaurant("山西面馆","面食")
r.describe_restaurant()
r.open_restaurant()
