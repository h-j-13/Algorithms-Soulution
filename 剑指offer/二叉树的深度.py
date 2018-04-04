# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    题目描述

    输入一棵二叉树，求该树的深度。
    从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
    """
    def TreeDepth(self, pRoot):
        # 边界判断
        depth = 0
        if not pRoot:
            return depth
        # 层序遍历
        pre_node_list = [pRoot]
        while pre_node_list:
            node_list = []
            for node in pre_node_list:
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
            pre_node_list = node_list
            depth += 1

        return depth