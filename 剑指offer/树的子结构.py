# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目描述

    输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
    """
    # todo 2018.4 重做一下这个题

    def treeEqual(self, root1, root2):
        # 简化问题,判断root1与root2是否是两颗相等的二叉树
        if not root2:  # root2遍历完成/递归出口
            return True
        if not root1 or root1.val != root2.val:
            return False
        return self.treeEqual(root1.left, root2.left) and self.treeEqual(root1.right, root2.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # 应该是个递归问题
        # 如果B是A以某个节点为根的子树(A')
        # 则 A' 的左子树 = B 的左子树 [递归判断]

        # 递归的逻辑：
        #   子树等于这个节点为根的树 or 等于这个节点左子树为根的树 or 等于这个节点右子树为根的树
        if not pRoot1 or not pRoot2:
            return False
        return self.treeEqual(pRoot1, pRoot2) or \
               self.HasSubtree(pRoot1.left, pRoot2) or \
               self.HasSubtree(pRoot1.right, pRoot2)


if __name__ == '__main__':
    tree1 = TreeNode(11)
    tree1.left = TreeNode(12)
    tree1.right = TreeNode(13)
    tree1.left.left = TreeNode(1)
    tree1.left.left.left = TreeNode(2)
    tree1.left.left.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    print Solution().treeEqual(tree1, None)
