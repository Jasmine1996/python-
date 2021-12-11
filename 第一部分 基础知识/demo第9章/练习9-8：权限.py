"""
练习9-8：权限 　编写一个名为Privileges 的类，它只有一个属性
privileges ，其中存储了练习9-7所述的字符串列表。将方法
show_privileges() 移到这个类中。在Admin 类中，将一个Privileges
实例用作其属性。创建一个Admin 实例，并使用方法show_privileges()
来显示其权限。
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


class Privileges:
    """一个存储管理员权限的类。"""
    def __init__(self, privileges=[]):
        # self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_rpivileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

class Admin(User):
    """有管理权限的用户。"""

    def __init__(self,first_name, last_name, username, email, location):
        """初始化管理员。"""
        super().__init__(first_name, last_name, username, email, location)
        # self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = Privileges()


admin = Admin("jasmine", "ming", "JASMINE", "XXX@XX.COM", "china")
admin.privileges.privileges = ["can add post", "can delete post", "can ban user"]
admin.privileges.show_rpivileges()

