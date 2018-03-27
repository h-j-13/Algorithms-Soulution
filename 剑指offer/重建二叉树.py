# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目描述

    输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
    """

    # 返回构造的TreeNode根节点

    def reConstructBinaryTree(self, pre, tin):
        # 前序遍历  : root-{left}-{right}
        # 中序遍历  : {left}-root-{right}
        # 应该是使用递归的思路做题,通过不断确定子节点的跟来填充二叉树

        if not pre:  # 边界判断
            return None

        if len(pre) == 1:  # 出口/递归出口 （叶子节点）
            return TreeNode(pre[0])

        root_value = pre[0]
        left_pre = pre[1:tin.index(root_value) + 1]
        right_pre = pre[len(left_pre) + 1:]
        left_tin = tin[0:tin.index(root_value)]
        right_tin = tin[tin.index(root_value) + 1:]

        root = TreeNode(pre[0])
        root.left = self.reConstructBinaryTree(left_pre, left_tin)
        root.right = self.reConstructBinaryTree(right_pre, right_tin)

        return root
