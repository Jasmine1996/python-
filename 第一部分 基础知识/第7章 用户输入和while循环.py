# 函数input（）的工作原理
message = input("Tell me something, and I willrepeat it back to you:")
print(message)


# greeter.py
name = input("Please enter your name:")
print(f"\nHello,{name.title()}!")

# 7.1.2 使用int（） 来获取数值输入
age = input("How old are you?")
age = int(age)
if age >=18:
    print(True)
elif age <40:
    print(False)
else:
    print(None)


# rollercoaster.py
height = input("How tall are you, in inches?")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


# 7.1.3 求模运算符
# >>> 4%3
# 1
# >>> 5%3
# 2
# >>> 6%3
# 0
# >>> 7*3
# 21
# >>> 7%3
# 1

# even_or_add.py
number = input("Enter a number,and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
