# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # 通过hash判断有无重复
        # O(n) O(n)
        tempList = []
        p = pHead
        while p:
            if p in tempList:
                return p
            else:
                tempList.append(p)
            p = p.next

        # # 数学题
        # # LinkedList = a1, a2, a3, a4, b1, b2, b3 ↷
        # #                            ↱ b6, b5, b4 ↲
        # # 快慢指针法 - 具体分析过程见LeetCode
        # # O(2n) O(1)
        # # 边界判断
        # if not pHead:
        #     return None
        # if pHead.next == pHead:
        #     return pHead
        # if not pHead.next or pHead.next.next:
        #     return None
        #
        # # 快慢链表在环中相遇
        # slow_cur = pHead.next
        # fast_cur = pHead.next.next
        # while fast_cur != slow_cur:
        #     if fast_cur.next and fast_cur.next.next:
        #         fast_cur = fast_cur.next.next
        #         slow_cur = slow_cur.next
        #     else:
        #         return None
        #
        # # 再从起始位置出发一个慢指针
        # slow_cur_2 = pHead
        # while slow_cur != slow_cur:
        #     slow_cur = slow_cur.next
        #     slow_cur_2 = slow_cur_2.next
        # return slow_cur
