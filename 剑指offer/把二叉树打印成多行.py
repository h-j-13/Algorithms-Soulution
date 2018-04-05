# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目描述

    从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
    """

    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # 层序遍历
        # 边界判断
        if not pRoot:
            return []
        result = []
        node_list = [pRoot]
        # 层序遍历
        while node_list:
            result_node = []
            next_node_list = []
            # left -> right
            for node in node_list:
                result_node.append(node.val)
                if node.left:
                    next_node_list.append(node.left)
                if node.right:
                    next_node_list.append(node.right)

            node_list = next_node_list
            result.append(result_node)
        # output
        return result
