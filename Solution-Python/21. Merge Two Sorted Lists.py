#!/usr/bin/env python
# encoding:utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2

        r = ListNode(-1)
        p = r

        while p1 or p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        if p1:
            p.next = p1
        else:
            p.next = p2

        return r.next

# 	20 ms	11.9 MB

# note
# 两个链表有序链表合并的题目，一般都是归并的思路
# 变种 1，一个增序，一个降序 ； 2， 奇数位置增序，偶数位置降序；

# better written

# Time:  O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # iteratively
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        start = None
        if l1.val < l2.val:
            start = l1;
            start.next = self.mergeTwoLists(l1.next, l2)
        else:
            start = l2;
            start.next = self.mergeTwoLists(l1, l2.next)

        return start