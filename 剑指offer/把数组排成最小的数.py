# -*- coding:utf-8 -*-

class Solution:
    """
    题目描述

    输入一个正整数数组，
    把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
    例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
    """

    def PrintMinNumber(self, numbers):
        # 判断 x,y 是否那个在前面,只需要判断 xy 大 还是 yx大即可得到结果
        # 先去掉 0 因为 0 肯定排在最前面
        if 0 in numbers:
            numbers.remove(0)
        numbers = map(str, numbers)
        numbers.sort(cmp=lambda x, y: cmp(x + y, y + x))
        return "".join(numbers)

        # 看了下讨论区 有个python的答案
        # 其实应该考虑 数组中有0的情况
        # 最后返回的表达式如下 先去除排序列表左边的中的 '0' 在产生结果
        # 其实可以先去掉啊 感觉...
        # return "".join(numbers).lstrip('0') or '0'
