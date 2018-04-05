# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
    其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
    不能使用除法。
    """

    def multiply(self, A):
        # 若能使用除法就是 B[i] = A元素累乘 / A[i]
        # 每一个元素硬算显然有点浪费时间
        # 通过矩阵找一下B组元素的特性
        B = []
        temp = 1
        # 下三角
        for Ai in A:
            B.append(temp)
            temp *= Ai
        # 上三角
        temp = 1
        for i in xrange(len(A) - 1, -1, -1):
            B[i] *= temp
            temp *= A[i]
        return B


print Solution().multiply([1, 2, 3, 4])
