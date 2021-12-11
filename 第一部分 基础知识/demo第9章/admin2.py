from user2 import User
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

