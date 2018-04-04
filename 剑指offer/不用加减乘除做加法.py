# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
    """

    def Add(self, num1, num2):
        # 肯定是位运算,具体过程参考<计算机组成原理>

        # Pythonic
        return sum((num1, num2))
