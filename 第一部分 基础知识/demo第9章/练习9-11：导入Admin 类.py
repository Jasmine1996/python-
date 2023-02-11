"""
练习9-11：导入Admin 类 　以为完成练习9-8而做的工作为基础。将User
类、Privileges 类和Admin 类存储在一个模块中，再创建一个文件，在其
中创建一个Admin 实例并对其调用方法show_privileges() ，以确认一切
都能正确运行。
"""

from user import Admin
admin = Admin("jasmine", "ming", "JASMINE", "XXX@XX.COM", "china")
admin.describe_user()
admin.privileges.privileges = ["can add post", "can delete post", "can ban user"]
admin.privileges.show_rpivileges()