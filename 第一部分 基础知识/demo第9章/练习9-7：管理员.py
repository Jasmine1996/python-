"""
练习9-7：管理员 　管理员是一种特殊的用户。编写一个名为Admin 的类，让
它继承为完成练习9-3或练习9-5而编写的User 类。添加一个名为
privileges 的属性，用于存储一个由字符串（如"can add post" 、"can
delete post" 、"can ban user" 等）组成的列表。编写一个名为
show_privileges() 的方法，显示管理员的权限。创建一个Admin 实例，
并调用这个方法。
"""

class User:
    """一个表示用户的简单类"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()


    def describe_user(self):
        """显示用户的摘要信息"""
        print(f"{self.first_name} {self.last_name}")
        print(f"  Username:{self.username}")
        print(f"  Email:{self.email}")
        print(f"  Location:{self.location}")


    def greet_user(self):
        """向用户发出个性化的问候。"""
        print(f"Hello {self.username}")


class Admin(User):
    """有管理权限的用户。"""
    def __init__(self,first_name, last_name, username, email, location):
        """初始化管理员。"""
        super().__init__(first_name, last_name, username, email, location)
        # self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = []
    def show_privileges(self):
        """显示当前管理员的权限。"""
        # print(f"{self.privileges}")
        print("Privileges")
        for i in self.privileges:
            print(f"- {i}")
admin = Admin("jasmine", "ming", "JASMINE", "XXX@XX.COM", "china")
admin.describe_user()
admin.privileges = ["can add post", "can delete post", "can ban user"]
admin.show_privileges()