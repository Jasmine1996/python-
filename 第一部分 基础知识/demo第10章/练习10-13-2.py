"""现在唯一的问题是嵌套了 if 语句。为解决这个问题，可将检查用户名是否正确的代
码移到另一个函数中。如果你觉得这个练习很有意思，可再尝试编写一个名为
check_username() 的函数，以免在 greet_user() 中嵌套 if 语句。"""

import json

def get_stored_username():
    """获取存储的用户名-- 如果存储了"""
    filename = '../dir_demo/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名。"""
    username = input("What is your name?")
    filename = '../dir_demo/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def check_user():
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}?(y/n) ")
        if correct == 'y':

def greet_user():
    """基于用户名问候用户。"""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}?(y/n) ")
        if correct == 'y':
            print(f"Welcome back,{username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back,{username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back,{username}!")
