# -*- coding:utf-8 -*-

class Solution:
    """
    题目描述

    一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
    """

    # 其实就是 0(1),1,2,4... 这个数列的前n项和
    # 跳到n层 = 0层(跳n) + 1层(跳n-1) + ... + n-1层(跳1)
    # 拿笔推算了一下，归纳出数学规律是 2^number-1
    def jumpFloorII(self, number):
        return pow(2, number - 1)

        # 补充一下python的位运算方式
        # return 1<<(number - 1)
