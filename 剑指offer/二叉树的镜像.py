# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目描述

    操作给定的二叉树，将其变换为源二叉树的镜像。
    """

    # 返回镜像树的根节点
    def Mirror_1(self, root):
        # 应该主要的思路就是递归与非递归的写法
        # 边界
        if root is None:
            return
        # swap
        root.left, root.right = root.right, root.left
        # 递归
        self.Mirror(root.left)
        self.Mirror(root.right)

        return root

    # 非递归方式
    def Mirror(self,root):
        # 按照层序遍历的思路
        # 把每层节点的左右互换,并存储下一次需要互换的节点

        # 边界
        if not root:
            return None
        # 存储本次互换的节点与下一次要互换的节点
        pre_root = [root]
        next_root = []

        # 类似层序遍历的思路，每次交换一层的节点
        while pre_root:
            while pre_root:
                temp = pre_root.pop()
                temp.left, temp.right = temp.right, temp.left
                # 不存none
                if temp.left:
                    next_root.append(temp.left)
                if temp.right:
                    next_root.append(temp.right)
            pre_root = next_root
            next_root = []
        return root