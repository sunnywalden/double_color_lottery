#!/bin/python
# -*- coding:utf-8 -*-

import unittest
from main.double_color_lottery_generator import random_shuangse


class Tests(unittest.TestCase):
    def test(self):
        lottery = random_shuangse(1)[0]
        red_nums = lottery[:5]
        #print(red_nums)
        for num in red_nums:
            #print(num)
            self.assertLess(num, 34, msg='red number is out of range')
            self.assertIsInstance(num, int, msg='red num is not int')
        self.assertLess(lottery[-1], 17, msg='blue number is out of range')
        self.assertIsInstance(num, int, msg='blue num is not int')


if __name__ == '__main__':
    unittest.main()
