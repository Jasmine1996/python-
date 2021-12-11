"""
练习9-5：尝试登录次数 　在为完成练习9-3而编写的User 类中，添加一个名
为login_attempts 的属性。编写一个名为
increment_login_attempts() 的方法，将属性login_attempts 的值
加1。再编写一个名为reset_login_attempts() 的方法，将属性
login_attempts 的值重置为0。

根据User 类创建一个实例，再调用方法increment_login_attempts()
多次。打印属性login_attempts 的值，确认它被正确地递增。然后，调用
方法reset_login_attempts() ，并再次打印属性login_attempts 的
值，确认它被重置为0。
"""

class User:
    """一个表示用户的简单类"""

    def __init__(self, first_name, last_name, username, email, location, login_attempts):
        """初始化用户"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = int(login_attempts)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        """显示用户的摘要信息"""
        print(f"{self.first_name} {self.last_name}")
        print(f"  Username:{self.username}")
        print(f"  Email:{self.email}")
        print(f"  Location:{self.location}")


    def greet_user(self):
        """向用户发出个性化的问候。"""
        print(f"Hello {self.username}")

user_1 = User("jasmine", "ming", "JASMINE","xxx@xx.com","china","2")
print(user_1.login_attempts)

user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)