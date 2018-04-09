# -*- coding:utf-8 -*-
import heapq


class Solution:
    """
    题目描述

    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
    那么中位数就是所有数值排序之后位于中间的数值。
    如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
    """
    def __init__(self):
        # 虽然Python heapq 只支持了 小顶堆的操作，
        # 但是可以讲进入大顶对的元素全部取反，
        # 取出时在取反
        # 就可以当成大顶堆使用
        self.smallerHeap = []  # 大顶堆
        heapq.heapify(self.smallerHeap)
        self.biggerHeap = []  # 小顶堆
        heapq.heapify(self.biggerHeap)

    def Insert(self, num):
        # write code here
        if len(self.smallerHeap) == len(self.biggerHeap):
            # 在smallerHeap里加入元素
            if len(self.biggerHeap) > 0 and num > self.biggerHeap[0]:
                tmpNum = heapq.heappushpop(self.biggerHeap, num)
                heapq.heappush(self.smallerHeap, -tmpNum)
            else:
                heapq.heappush(self.smallerHeap, -num)  # 大顶堆，使用相反数
        else:
            # 在biggerHeap里加入元素
            if len(self.smallerHeap) > 0 and num < -self.smallerHeap[0]:
                tmpNum = heapq.heappushpop(self.smallerHeap, -num)
                heapq.heappush(self.biggerHeap, -tmpNum)
            else:
                heapq.heappush(self.biggerHeap, num)

    def GetMedian(self, x):
        # write code here
        size = len(self.smallerHeap) + len(self.biggerHeap)
        if size & 0x1 == 0:  # 偶数
            return (-self.smallerHeap[0] + self.biggerHeap[0]) / 2.0
        else:
            return -self.smallerHeap[0]