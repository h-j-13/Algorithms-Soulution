# -*- coding:utf-8 -*-
import heapq


class Solution:
    """
    题目描述

    输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
    """

    def GetLeastNumbers_Solution(self, tinput, k):
        # TOP N 问题 - 堆
        # 自己写了挺多遍了,去网上找了一下python竟然有内置的堆实现 >> heapq

        # 边界处理
        if k > len(tinput):
            return []
        heapq.heapify(tinput)
        min_k = []
        for i in xrange(k):
            min_k.append(heapq.heappop(tinput))
        return min_k


print Solution().GetLeastNumbers_Solution([1, 2, 3, 4, 5], 4)
