# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，
    如果有多对数字的和等于S，输出两个数的乘积最小的。
    """

    def FindNumbersWithSum(self, array, tsum):
        # 头尾指针
        left = 0
        right = len(array) - 1
        while left <= right:
            if array[left] + array[right] == tsum:
                return [array[left], array[right]]
            elif array[left] + array[right] > tsum:
                right -= 1
            else:
                left += 1
        return []
