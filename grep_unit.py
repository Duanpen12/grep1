import unittest
# import re
import re


def fun(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)


def element_had_a_q(text):
    result_list = []
    match_list = re.finditer(r'\b(\w*q\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(1))
        return result_list


word_element_had_a_q = element_had_a_q("Iraq is a country located in the Middle East leopard"
                                       "In the Middle East leopard Mosque "
                                       "Banana pie qaids banana pie")

# print(word_element_had_a_q)

class RegexFunctionElementQTest(unittest.TestCase):
    def test_word_element_had_q_last(self):
        self.assertEqual(
            element_had_a_q("Iraq is a country located in the Middle East leopard"), ["Iraq"])

    def test_word_element_had_q_middle(self):
        self.assertEqual(
            element_had_a_q("in the Middle East leopard Mosque"), ["Mosque"])


# def containing_the_string_start_cl(text):
#     result_list = []
#     match_list = re.finditer(r'.*^Cl.*\w+', text)
#     if match_list:
#         for match in match_list:
#             result_list.append(match.group(1))
#         return result_list
#
#
# match_with_text = open('people.txt', 'r')
# content = match_with_text.readlines()
# print(content)

def add(x, y):
    return x + y


def multipy(x, y):
    return x * y


def divi(x, y):
    return x / y


def minus(x, y):
    return x - y






if __name__ == '__main__':
    unittest.main()
    assert 5 == add(3, 2)
    assert 6 == multipy(3, 2)
    assert 10 == minus(20, 10)
    assert 5 == divi(10, 2)
