# 11 测试代码
# 使用Python模块unittest 中的工具来测试代码

# 11.1 测试函数
# name_function.py
def get_formatted_name(first, last):
    """生成整洁的姓名。"""
    full_name = f"{first} {last}"
    return full_name.title()


# names.py
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        break
    last = input("Please give me a last name:")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")


# 11.1.1 单元测试和测试用例
"""
Python标准库中的模块unittest 提供了代码测试工具。单元测试 用于核实函数的
某个方面没有问题。测试用例 是一组单元测试，它们一道核实函数在各种情形下的
行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，包含针对所
有这些情形的测试。全覆盖 的测试用例包含一整套单元测试，涵盖了各种可能的函
数使用方式。对于大型项目，要进行全覆盖测试可能很难。通常，最初只要针对代
码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。
"""

# 11.1.2 可用过的测试
# test_name_function.py
import unittest

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确的处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()


