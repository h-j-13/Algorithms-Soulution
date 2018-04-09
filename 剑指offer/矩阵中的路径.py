# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
    路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
    如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
    例如
    a b c e
    s f c s
    a d e e
    矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
    因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
    """

    def hasPath(self, matrix, rows, cols, path):
        # 用二维数组记录访问的过程
        for i in range(rows):
            for j in range(cols):
                # 遍历矩阵,找到所有的字符串第一个字符,作为路径的起始位置
                if matrix[i * cols + j] == path[0]:
                    if self.find(list(matrix), rows, cols, path[1:], i, j):  # 这里传入了一个矩阵的副本
                        return True
        return False

    def find(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i * cols + j] = '0'  # 访问过的元素置为0
        if j + 1 < cols and matrix[i * cols + j + 1] == path[0]:  # right
            return self.find(matrix, rows, cols, path[1:], i, j + 1)
        elif j - 1 >= 0 and matrix[i * cols + j - 1] == path[0]:  # left
            return self.find(matrix, rows, cols, path[1:], i, j - 1)
        elif i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:  # down
            return self.find(matrix, rows, cols, path[1:], i + 1, j)
        elif i - 1 >= 0 and matrix[(i - 1) * cols + j] == path[0]:  # up
            return self.find(matrix, rows, cols, path[1:], i - 1, j)
        else:   # 越界,死路
            return False

    添加笔记
