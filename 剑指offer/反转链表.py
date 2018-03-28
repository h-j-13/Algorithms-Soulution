# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # 维护两个链表指针即可... 感觉没什么可优化的地方
        # 链表题目尽量不是要使用额外空间!

        cur = pHead
        reverse_cur = None

        while cur != None:
            temp = cur
            # swap
            cur = cur.next
            temp.next = reverse_cur
            reverse_cur = temp

        return reverse_cur
