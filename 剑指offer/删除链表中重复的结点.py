# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    题目描述

    在一个排序的链表中，存在重复的结点，
    请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
    例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
    """
    #　递归方式
    def deleteDuplication(self, pHead):
        # 边界判断
        if not pHead or not pHead.next:
            return pHead

        # 判断当前节点是否是重复节点
        if pHead.val == pHead.next.val:
            cur = pHead.next
            # 找到下一个与节点数值不同的节点
            while cur and cur.val == pHead.val:
                cur = cur.next
            return self.deleteDuplication(cur)
        else:   # 当前节点不是重复节点
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead

