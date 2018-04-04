# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目描述

    请实现一个函数按照之字形打印二叉树，
    即第一行按照从左到右的顺序打印，
    第二层按照从右至左的顺序打印，
    第三行按照从左到右的顺序打印，其他行以此类推。
    """

    def Print(self, pRoot):
        # 层序遍历的高阶版本
        # 若是每层都是从左到右记录 再反转偶数层的话
        # 则不如偶数层直接就从右到左记录
        # 则需要一个能前后插入元素的双端队列
        # python的list 插入后面:append() 插入前面:insert(0)

        # 边界判断
        if not pRoot:
            return []
        order_is_left2right = True
        result = []
        node_list = [pRoot]
        # 层序遍历
        while node_list:
            result_node = []
            next_node_list = []
            if order_is_left2right:  # left -> right
                for node in node_list:
                    result_node.append(node.val)
                    if node.left:
                        next_node_list.append(node.left)
                    if node.right:
                        next_node_list.append(node.right)
                order_is_left2right = False
            else:
                for node in node_list:  # right -> left
                    result_node.insert(0, node.val)
                    if node.left:
                        next_node_list.append(node.left)
                    if node.right:
                        next_node_list.append(node.right)
                order_is_left2right = True
            node_list = next_node_list
            result.append(result_node)
        # output
        return result
