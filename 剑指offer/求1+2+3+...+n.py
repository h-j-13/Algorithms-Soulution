# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字
    及条件判断语句（A?B:C）
    """

    def Sum_Solution(self, n):
        # 等差数列通项公式 (n + 1) * n / 2
        # n + 1 和 / 2 都比较好办 要算 * n 可以把 n 拆分成 2^i (0<=i<=log2n)的方式
        # 在通过位运算计算即可 不过要事先知道 n 的 范围才能把它拆分成2的多少次方的形式
        # 懒得写了..
        # 　return ((n + 1) * 2) >> 1

        # pythonnic
        # return sum(range(1, n + 1))

        # 正规思路应该是使用 && 短路　+　递归的形式
        # python 的and还有这个形式...
        # a and b = b (b>a)
        return n and self.Sum_Solution(n - 1) + n
