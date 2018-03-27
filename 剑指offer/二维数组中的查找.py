#!/usr/bin/env python
# encoding:utf-8

class Solution:
    """
    题目描述

    在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

    """

    def Find(self, target, array):
        # 讨论区里有说是整个矩阵都是有序的，那么从左下角开始比较应该是最快的 O(长+宽)
        # 如果从左上角开始的话,当target大于当前值时，会有两个前进方向 → 和 ↓
        # 所以 左下角和右上角是两个比较好的开始位置

        try:
            cow = len(array) - 1
            line = 0
            temp = array[cow][line]

            while 1:
                if target == temp:
                    return True
                elif target > temp:  # →
                    line += 1
                    temp = array[cow][line]
                elif target < temp:  # ↑
                    cow -= 1
                    temp = array[cow][line]

        except IndexError as e:
            return False

    # best
    # 看了一下最佳答案 直接用 in 查找竟然是最快的...看起来牛客网这个测试系统也不是很好。。
    # pythonic..

    def BEST_Find(self, target, array):
        for line in array:
            if target in line:
                return True
        return False