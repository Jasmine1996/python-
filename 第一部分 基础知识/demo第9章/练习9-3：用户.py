"""
练习9-3：用户 　创建一个名为User 的类，其中包含属性first_name 和
last_name ，以及用户简介通常会存储的其他几个属性。在类User 中定义一
个名为describe_user() 的方法，用于打印用户信息摘要。再定义一个名为
greet_user() 的方法，用于向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
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

user_1 = User("jasmine", "ming" ,"JASMINE","xxx@xx.com", "china")
user_1.describe_user()
user_1.greet_user()