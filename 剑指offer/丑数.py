# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    把只包含因子2、3和5的数称作丑数（Ugly Number）。
    例如6、8都是丑数，但14不是，因为它包含因子7。
    习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
    """

    def GetUglyNumber_Solution(self, index):
        # 丑数的定义是1或者因子只有2 3 5，可推出丑数=丑数*丑数，假定丑数有序序列为：a1,a2,a3.......an
        # 所以可以将以上序列（a1除外）可以分成3类，必定满足：
        # 包含2的有序丑数序列：2*a1, 2*a2, 2*a3 .....
        # 包含3的有序丑数序列：3*a1, 3*a2, 3*a3 .....
        # 包含5的有序丑数序列：5*a1, 5*a2, 5*a3 .....
        # 以上3个序列的个数总数和为n个，而且已知a1 = 1了，将以上三个序列合并成一个有序序列即可 
        # 程序中t2,t3,t5实际就是合并过程中三个序列中带排序的字段索引

        if index < 7:
            return index

        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        for i in xrange(1, index):
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
            if ugly[i] == ugly[i2] * 2:
                i2 += 1
            if ugly[i] == ugly[i3] * 3:
                i3 += 1
            if ugly[i] == ugly[i5] * 5:
                i5 += 1

        return ugly[index - 1]
