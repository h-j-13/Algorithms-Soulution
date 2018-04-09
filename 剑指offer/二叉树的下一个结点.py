# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    """
    题目描述

    给定一个二叉树和其中的一个结点，
    请找出中序遍历顺序的下一个结点并且返回。
    注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
    """

    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:  # 如果有右子树，则找右子树的最左节点
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        else:  # 如果没右子树，则找第一个当前节点是父节点左孩子的节点
            while pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                pNode = pNode.next
            return None
