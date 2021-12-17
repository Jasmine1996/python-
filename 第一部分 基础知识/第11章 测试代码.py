# 11 测试代码
# 使用Python模块unittest 中的工具来测试代码

# 11.1 测试函数
# name_function.py
# def get_formatted_name(first, last):
#     """生成整洁的姓名。"""
#     full_name = f"{first} {last}"
#     return full_name.title()

def get_formatted_name(first, last, middle=''):
    """生成整洁的姓名"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

# names.py
# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name:")
#     if first == 'q':
#         break
#     last = input("Please give me a last name:")
#     if last == 'q':
#         break
#     formatted_name = get_formatted_name(first, last)
#     print(f"\tNeatly formatted name: {formatted_name}.")


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
    def test_first_last_middle_name(self):
        """能够正确的处理像Wolfgang Amadeus Mozart 这样的姓名么？"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus'
        )
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
if __name__ == '__main__':
    unittest.main()



# 11.3 未通过的测试
# name_function.py
# def get_formatted_name(first, middle, last):
#     """生成整洁的姓名"""
#     full_name = f"{first} {middle} {last}"
#     return full_name.title()


# 11.4 测试未通过时怎么办


# 11.1.5 添加新测试



# 11.2 测试类
"""
Python在unittest.TestCase 类中提供了很多断言方法。前面说过，断言方法检
查你认为应该满足的条件是否确实满足。如果该条件确实满足，你对程序行为的假
设就得到了确认，可以确信其中没有错误。如果你认为应该满足的条件实际上并不
满足，Python将引发异常"""

# 11.2.2 一个要测试的类
class_name = 'demo第11章/survey.py'

# 11.2.3
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    "针对AnonymousSurvey 类的测试。"
    def test_store_single_response(self):
        """测试单个答案会被妥善的存储。"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """测试三个大那会被妥善的存储。"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

    if __name__ == '__main__':
        unittest.main()


# 11.2.4 方法setUp（）
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    "针对AnonymousSurvey 类的测试。"
    def setUp(self) -> None:
        """创建一个调查对象和一组答案，供使用的测试方法使用。"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善的存储。"""
        # question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(self.responses[0])
        self.assertIn(self.responses[0], my_survey.responses)

    def test_store_three_responses(self):
        """测试三个大那会被妥善的存储。"""
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # responses = ['English', 'Spanish', 'Mandarin']
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

    if __name__ == '__main__':
        unittest.main()

