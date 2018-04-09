# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    地上有一个m行和n列的方格。
    一个机器人从坐标0,0的格子开始移动，
    每一次只能向左，右，上，下四个方向移动一格，
    但是不能进入行坐标和列坐标的数位之和大于k的格子。

    例如，当k为18时，机器人能够进入方格（35,37），
    因为3+5+3+7 = 18。但是，它不能进入方格（35,38），
    因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
    """

    def movingCount(self, threshold, rows, cols):
        # 边界
        if threshold < 0:
            return 0

        # 用一个二维矩阵记录访问的情况
        matrix = []
        for i in xrange(rows):
            matrix.append([0 for j in xrange(cols)])
        nodes = [(0, 0)]
        matrix[0][0] = 1
        while nodes:
            next_nodes = []
            for i, j in nodes:
                print i, j
                # 　检测这个节点是否还能继续走
                if i - 1 >= 0 and matrix[i - 1][j] == 0 and self.bitSum(i - 1, j) <= threshold:  # up
                    next_nodes.append((i - 1, j))
                    matrix[i - 1][j] = 1
                if i + 1 < rows and matrix[i + 1][j] == 0 and self.bitSum(i + 1, j) <= threshold:  # down
                    next_nodes.append((i + 1, j))
                    matrix[i + 1][j] = 1
                if j - 1 >= 0 and matrix[i][j - 1] == 0 and self.bitSum(i, j - 1) <= threshold:  # left
                    next_nodes.append((i, j - 1))
                    matrix[i][j - 1] = 1
                if j + 1 < cols and matrix[i][j + 1] == 0 and self.bitSum(i, j + 1) <= threshold:  # right
                    next_nodes.append((i, j + 1))
                    matrix[i][j + 1] = 1
            nodes = next_nodes
        count = 0
        for c in matrix:
            count += c.count(1)
        return count

    def bitSum(self, n, m):
        return sum(int(i) for i in list(str(n) + str(m)))


if __name__ == '__main__':
    print Solution().movingCount(100, 100, 100)
