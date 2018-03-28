# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
    """

    # 还有一个隐藏条件,2进制长为32位

    def NumberOf1(self, n):
        # 第一个思路，使用bin()
        # bin() |  n -> str:'0b10101...'

        # if n < 0:   # 根据补码的性质 2^32 = 11111111
        #     return list(bin(2**32+(n)))[2:].count('1')
        # else:
        #     return list(bin(n))[2:].count('1')

        # 分别判断32位的二进制是否为1,然后相加
        # 考察位运算
        result = 0
        for i in xrange(32):  # 判断每一位是否为1 （按位向右移并与1(00000001)判断该位是否为1）
            result += n >> i & 1
        return result

        # 或者再简化一点
        return sum([n >> i & 1 for i in xrange(32)])


if __name__ == '__main__':
    print Solution().NumberOf1(-1)
