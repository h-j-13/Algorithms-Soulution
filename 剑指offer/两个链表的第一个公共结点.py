# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    题目描述

    输入两个链表，找出它们的第一个公共结点。
    """

    def FindFirstCommonNode(self, pHead1, pHead2):
        # 可以用hash记录两链表节点在 找到第一次相同的节点 O(n+m) O(n)
        # 或者分别用两个指针遍历链表，根据特性找到距离链表尾相同的店
        # A : a1-a2-a3-a4-a5-c1-c2-c...
        # B : b1-b2-c1-c2-c...
        cur_1 = pHead1
        cur_2 = pHead2
        cur_1_longer = True
        length_diff = 0
        # 获取两链表长度差
        while cur_1 is not None and cur_2 is not None:
            cur_1 = cur_1.next
            cur_2 = cur_2.next
        if cur_2 is not None:
            cur_1_longer = False
        if cur_1_longer:
            while cur_1 is not None:
                cur_1 = cur_1.next
                length_diff += 1
        else:
            while cur_2 is not None:
                cur_2 = cur_2.next
                length_diff += 1
        # 长的链表先出发
        cur_1 = pHead1
        cur_2 = pHead2
        if cur_1_longer:
            while length_diff:
                length_diff -= 1
                cur_1 = cur_1.next
        else:
            while length_diff:
                length_diff -= 1
                cur_2 = cur_2.next
        # 找到相同节点,或者直到最后共同到达None
        while cur_1 != cur_2:
            cur_1 = cur_1.next
            cur_2 = cur_2.next
        return cur_1
