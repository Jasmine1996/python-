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


