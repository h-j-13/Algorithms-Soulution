# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目描述

    从上往下打印出二叉树的每个节点，同层节点从左至右打印。
    """

    # 感觉和层序遍历一个思路

    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # 边界判断
        if root is not None:
            queue = [root]
        else:
            return []

        result = []
        queue_temp = []

        while queue:
            while queue:
                temp = queue.pop(0)
                if temp.left is not None:  # 每一层 左先进 右再进
                    queue_temp.append(temp.left)
                if temp.right is not None:
                    queue_temp.append(temp.right)
                result.append(temp.val)  # 访问这个节点
            queue = queue_temp
        return result
