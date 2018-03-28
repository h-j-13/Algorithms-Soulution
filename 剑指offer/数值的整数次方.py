# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
    """

    def Power(self, base, exponent):
        # 1. 朴素 O(exponent)
        # 这样就能过... 忘了c++里 pow()函数支不支持基数是非整形了

        # return pow(base, exponent)

        # 2. 快速幂算法 O(log2exponent)
        # 顾名思义，快速幂就是快速算底数的n次幂。其时间复杂度为 O(log₂N)， 与朴素的O(N)相比效率有了极大的提高。
        # 信息安全数学基础上提到过的算法（只能算正整数幂）
        # a^11 = a^(2^0+2^1+2^3) = a^2 * a^2 * a^8    // 11 = 1 + 2 + 8
        # 主要是使用前面计算的结果来加速运算 当然指数小于0也一样适用

        # 那么只要求出这个指数的二进制表达即可,用到了前一题的知识
        # 时间复杂度取决于指数的二进制位数

        # if exponent >= 0:  # >= 0
        #     exponent_bin_str = bin(exponent)[2:]
        #     base_table = [base, 1]
        # else:  # < 0
        #     exponent_bin_str = bin(exponent)[3:]
        #     base_table = [1.0 / base, 1]
        # # 求出 base * 2^i 的结果  0<=i<=len(exponent_bin_str)
        # for i in xrange(1, len(exponent_bin_str)):  # note: xrange(3,2)这样些是不会报错的，只会返回一个迭代完的对象
        #     base_table.insert(0, base_table[0] ** 2)
        #
        # result = 1
        # for base_table_item, index in zip(base_table, list(exponent_bin_str)):
        #     if index == '1':
        #         result *= base_table_item
        #
        # return result

        # 3. 递归
        # 当然这个递归也可以加速一下.. 使用lru 或者 cache 就像前几题那样 不过这一题不会有重复用到某个递归结果好几次的情况
        # 当 exponent 等于偶数时 result = base^exponent/2 * base^exponent/2
        #             等于奇数时 result = base^exponent-1/2 * base^exponent-1/2 * base

        # 递归出口
        if exponent == 1:
            return base
        elif exponent == -1:
            return 1.0 / base
        elif exponent == 0:  # 边界判断
            return 1

        if exponent % 2 == 0:
            return self.Power(base, exponent / 2) ** 2
        else:
            return self.Power(base, (exponent - 1) / 2) ** 2 * base


if __name__ == '__main__':
    print Solution().Power(2, -3)
