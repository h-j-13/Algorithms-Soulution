# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目描述

    给定一颗二叉搜索树，请找出其中的第k大的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。
    """

    def __init__(self):
        self.node = []

    def LDR(self, pRoot):
        if not pRoot:
            return
        self.LDR(pRoot.left)
        self.node.append(pRoot)
        self.LDR(pRoot.right)

    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # 二叉树的中序遍历 左-中-右 正好是从小到大的顺序 取第k个值
        self.LDR(pRoot)
        return self.node[k - 1] if 0 < k <= len(self.node) else None
