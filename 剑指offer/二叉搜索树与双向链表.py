# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目描述

    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
    """
    def __init__(self):
        self.left_node = None
        self.pre_node = None

    def Convert(self, pRootOfTree):
        # 二叉搜索树的有序遍历就是中序遍历 左-中-右
        # 采用中序递归遍历的方式,并用一个临时变量记录上次访问的节点指针.
        # 当前结点指向左指针指向前驱结点
        # 前驱结点右指针指向当前结点

        # 边界判断
        if not pRootOfTree:
            return None
        # 中序遍历
        self.Convert(pRootOfTree.left)
        if not self.left_node:
            self.left_node = pRootOfTree
        if self.pre_node:
            self.pre_node.right = pRootOfTree
        pRootOfTree.left = self.pre_node
        self.pre_node = pRootOfTree
        self.Convert(pRootOfTree.right)

        return self.left_node