# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
    例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
    """

    # matrix类型为二维列表，需要返回列表
    def __init__(self):
        self.result = []

    def printMatrixItem(self, matrix, cur_index):
        # 访问矩阵特定元素
        self.result.append(matrix[cur_index[0]][cur_index[1]])

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # 获取长宽
        matrix_y = len(matrix)
        matrix_x = len(matrix[0])
        if matrix_x == 1 and matrix_y == 1:
            return matrix[0]
        cur_index = [0, 0]
        self.goMatrix(matrix, matrix_x, matrix_y, cur_index)
        return self.result

    # 按照刚才的思路继续,只不过这次上下移动的时候看y长 左右移动的时候看x长
    def goMatrix(self, matrix, x, y, cur_index):
        # 递归出口
        if x <= 0 or y <= 0:
            return
        elif x == y == 1:  # 最后只有一个元素,不用再转圈了
            self.printMatrixItem(matrix, cur_index)
            return
        # 右
        for times in xrange(x - 1):
            self.printMatrixItem(matrix, cur_index)
            cur_index[1] += 1
        # 下
        for times in xrange(y - 1):
            self.printMatrixItem(matrix, cur_index)
            cur_index[0] += 1
        # 左
        if y - 1 != 0:  # 处理只有一行的特殊情况
            for times in xrange(x - 1):
                self.printMatrixItem(matrix, cur_index)
                cur_index[1] -= 1
        else:
            self.printMatrixItem(matrix, cur_index)

        # 上
        if x - 1 != 0:
            for times in xrange(y - 1):
                self.printMatrixItem(matrix, cur_index)
                cur_index[0] -= 1
        else:
            self.printMatrixItem(matrix, cur_index)
        # 最后回到了起始位置
        # 变更到下一次访问外圈的位置
        cur_index[0] += 1
        cur_index[1] += 1
        # 变更到下一次访问外圈的长度
        x -= 2
        y -= 2
        self.goMatrix(matrix, x, y, cur_index)


    # 看到一个比较好的思路

    #可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
    # 例如
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 输出并删除第一行后，再进行一次逆时针旋转，就变成：
    # 6 9
    # 5 8
    # 4 7
    # 继续重复上述操作即可
    #

    # 思路很清晰，不过感觉这个旋转比较费时间 时间复杂度不是O(n)了

    # class Solution:
    #     # matrix类型为二维列表，需要返回列表
    #     def printMatrix(self, matrix):
    #         # write code here
    #         result = []
    #         while (matrix):
    #             result += matrix.pop(0)
    #             if not matrix or not matrix[0]:
    #                 break
    #             matrix = self.turn(matrix)
    #         return result
    #
    #     def turn(self, matrix):
    #         num_r = len(matrix)
    #         num_c = len(matrix[0])
    #         newmat = []
    #         for i in range(num_c):
    #             newmat2 = []
    #             for j in range(num_r):
    #                 newmat2.append(matrix[j][i])
    #             newmat.append(newmat2)
    #         newmat.reverse()
    #         return newmat






    # 最后发现说的矩阵的意思是包括长方形...好好读题！

    # def printMatrix(self, matrix):
    #     # 怎么感觉最后是数学规律的题目..
    #     # 既然要遍历一遍输出,时间复杂度最低也是O(N)了
    #
    #     # 边界 - 退化为1维数组的情况
    #     edge_length = len(matrix)  # 矩阵的长宽应该是一样的
    #     if edge_length == 1:
    #         return matrix[0]
    #     cur_index = [0, 0]  # 纵,横坐标
    #     # 每一次遍历外面一圈都是一样的流程,把他抽离出来一个函数
    #     # 每次开始走的时候,都是从(0,0)(1,1)(2,2这个位置开始走的) 对应的边长分别为
    #     # 很明显 这个函数最后一次走一圈的边长是2，而且每次边长都会-2
    #     # 应该可以写成递归 上面就是边界判断条件
    #     self.goMatrix(matrix, edge_length, cur_index)
    #     return self.result
    #
    # def printMatrixItem(self, matrix, cur_index):
    #     # 访问矩阵特定元素
    #     self.result.append(matrix[cur_index[0]][cur_index[1]])
    #
    # def goMatrix(self, matrix, edge_length, cur_index):
    #     # 递归出口
    #     if edge_length == 0:
    #         return
    #     elif edge_length == 1:  # 最后只有一个元素,不用再转圈了
    #         self.printMatrixItem(matrix, cur_index)
    #         return
    #     # 右
    #     for times in xrange(edge_length - 1):
    #         self.printMatrixItem(matrix, cur_index)
    #         cur_index[1] += 1
    #     # 下
    #     for times in xrange(edge_length - 1):
    #         self.printMatrixItem(matrix, cur_index)
    #         cur_index[0] += 1
    #     # 左
    #     for times in xrange(edge_length - 1):
    #         self.printMatrixItem(matrix, cur_index)
    #         cur_index[1] -= 1
    #     # 上
    #     for times in xrange(edge_length - 1):  # 向上只能走 edge_length - 2个节点
    #         self.printMatrixItem(matrix, cur_index)
    #         cur_index[0] -= 1  # 最后回到了起始位置
    #     # 变更到下一次访问外圈的位置
    #     cur_index[0] += 1
    #     cur_index[1] += 1
    #     # 变更到下一次访问外圈的长度
    #     edge_length -= 2
    #     self.goMatrix(matrix, edge_length, cur_index)


if __name__ == '__main__':
    test = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

    print Solution().printMatrix(test)
