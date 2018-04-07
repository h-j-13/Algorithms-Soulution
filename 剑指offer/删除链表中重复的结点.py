# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # 用两个指针来跨过数值相等的区域

        # 边界判断
        if not pHead or not pHead.next:
            return pHead

        # 给链表加一个头，以防开头就有重复元素
        result = ListNode(-1)
        result.next = pHead

        cur = result
        cur1 = pHead
        cur2 = pHead.next

        while cur:
            # cur2 一直向后直到找到第一个与cur1不相同的节点
            while cur1.val == cur2.val:
                cur2 = cur2.next
            cur1 =






        while cur1 is not None:
            # cur2 一直向后知道找到第一个与cur1不相同的节点
            while cur2 is not None and cur2.val == cur1.val:
                cur2 = cur2.next
            cur1.next = cur2
            if cur2 is not None:
                cur2 = cur2.next
                cur1 = cur1.next
            else:
                break
        return pHead
