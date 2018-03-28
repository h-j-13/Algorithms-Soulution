# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    题目描述

    输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
    """

    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        result_cur = ListNode(-1)
        cur = result_cur

        while pHead1 is not None and pHead2 is not None:
            if pHead1.val >= pHead2.val:
                cur.next = pHead2
                pHead2 = pHead2.next
            else:
                cur.next = pHead1
                pHead1 = pHead1.next
            cur = cur.next

        if pHead1 is not None:
            cur.next = pHead1
        else:
            cur.next = pHead2

        return result_cur.next


if __name__ == '__main__':
    a = ListNode(1)
    t1 = a
    a.next = ListNode(3)
    a = a.next
    a.next = ListNode(5)
    a = a.next
    b = ListNode(2)
    t2 = b
    b.next = ListNode(4)
    b = b.next
    b.next = ListNode(6)
    b = b.next

    x = Solution().Merge(t1,t2)

    c = 1