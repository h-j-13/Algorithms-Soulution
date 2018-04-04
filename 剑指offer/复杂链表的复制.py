# -*- coding:utf-8 -*-

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    """
    题目描述

    输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
    返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）"""

    # 返回 RandomListNode
    def Clone(self, pHead):
        # 评论区看到的思路 把 A->B->C 变成 A->A'->B->B'->C->C'
        # 再出里random指针 若 A.random = C 则 A.next.random = A.random.next
        if not pHead:
            return None
        # 　在每个节点后面增加复制节点
        cur = pHead
        while cur:
            copyNode = RandomListNode(cur.label)
            copyNode.next = cur.next
            cur.next = copyNode
            cur = copyNode.next
        #   处理random指针
        cur = pHead
        while cur:
            copyList = cur.next
            if cur.random:
                copyList.random = cur.random.next
            cur = copyList.next
        #   拆分结果链表
        cur = pHead
        result = pHead.next
        while cur.next:
            temp = cur.next
            cur.next = temp.next
            cur = temp

        return result

        # 感觉下面的解法都不符合题意 包括讨论区的hash解法,有可能出现链表节点相同的情况
        # 递归 O(n)
        # =============================
        if not pHead:
            return None
        else:
            result = RandomListNode(pHead.label)
            # 其实这里不太对
            # 这里只复制了pHead指向的地址 实际应该是深度复制
            result.random = pHead.random
            result.next = self.Clone(pHead.next)
        return result

        # 朴素的思路 O(2n) 超时
        # =============================
        cur = pHead
        result = None
        first_node = True
        result_pHead = None
        # 先复制一遍链表 忽略 random指针
        while cur is not None:
            result = RandomListNode(pHead.label)
            if first_node:
                result_pHead = result
                first_node = False
            result = result.next
            cur = pHead.next
        # 再处理 random 指针
        cur = pHead
        result = result_pHead
        while cur is not None:
            result.random = cur.random
            cur = cur.next
            result = result.none

        return result_pHead
