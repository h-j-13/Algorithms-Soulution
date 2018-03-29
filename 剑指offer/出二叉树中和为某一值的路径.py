# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目描述

    输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
    路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
    """

    def __init__(self):
        self.result = []

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # 边界判断
        if root is None:
            return []

        # 递归出口
        road = []
        self.FindPathInTree(root, expectNumber, road)

        # 因为左右子树均会添加一次节,每隔一个元素去重
        return [result for index, result in enumerate(self.result) if index % 2 == 1]

    def FindPathInTree(self, root, expectNumber, now_road):
        # 递归出口
        now_road_copy = now_road[:]
        if root is None:  # 走到叶子节点了
            if expectNumber == 0:
                self.result.append(now_road_copy)
            return

        else:  # 继续访问左，右子树 并修改期望值
            now_road_copy.append(root.val)
            self.FindPathInTree(root.left, expectNumber - root.val, now_road_copy)
            self.FindPathInTree(root.right, expectNumber - root.val, now_road_copy)


if __name__ == '__main__':
    for i, j in enumerate(['a', 'b']):
        print i,
        print j

    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)

    print Solution().FindPath(t, 3)
