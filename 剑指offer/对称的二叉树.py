# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目描述

    请实现一个函数，用来判断一颗二叉树是不是对称的。
    注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
    """

    def isSymmetrical(self, pRoot):
        # 边界判断
        if not pRoot:
            return True
        else:
            return self.TreeIsSymmetrical(pRoot.left, pRoot.right)

    def TreeIsSymmetrical(self, node1, node2):
        """判断两节点为根的二叉树是不是对称的"""
        if not node1 and not node2:
            return True
        elif node1 and node2:
            return node1.val == node2.val and \
                   self.TreeIsSymmetrical(node1.left, node2.right) and \
                   self.TreeIsSymmetrical(node1.right, node2.left)
        else:
            return False
