"""
练习9-12：多个模块 　将User 类存储在一个模块中，并将Privileges 类 和Admin 类存储在另一个模块中。再创建一个文件，在其中创建一个Admin
实例并对其调用方法show_privileges() ，以确认一切依然能够正确运行。
"""

from admin2 import Admin
from user2 import User

admin =Admin("jasmine", "ming", "JASMINE", "XXX@XX.COM", "china")
admin.describe_user()
admin.privileges.show_rpivileges()