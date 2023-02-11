"""
练习9-13：骰子 　创建一个Die 类，它包含一个名为sides 的属性，该属性
的默认值为6。编写一个名为roll_die() 的方法，它打印位于1和骰子面数之
间的随机数。创建一个6面的骰子再掷10次。
创建一个10面的骰子和一个20面的骰子，再分别掷10次。
"""
from random import randint
class Die:
    """创建一个骰子类"""
    def __init__(self, sides=6):
        """初始化骰子类"""
        self.sides = sides

    def roll_die(self, count):
        """模拟摇扇子的动作，输出 摇的数"""
        for _ in range(count):
            num = randint(1, self.sides)
            print(num)

die = Die(20)
die.roll_die(1)

