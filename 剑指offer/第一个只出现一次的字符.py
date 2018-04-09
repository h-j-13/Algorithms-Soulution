# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    在一个字符串(1<=字符串长度<=10000，全部由字母组成)
    中找到第一个只出现一次的字符,并返回它的位置
    """

    def FirstNotRepeatingChar(self, s):
        # 懒得动脑了.. Pythonic
        if not s:
            return -1

        for char in s:
            if s.count(char) == 1:
                return s.index(char)
