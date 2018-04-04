# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
    由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
    如果不存在则输出0。

    """

    def MoreThanHalfNum_Solution(self, numbers):
        # 用dict记录各个数字出现次数
        # O(n) O(n)
        num_count = {}
        numbers_length = len(numbers)
        for num in numbers:
            if num_count.has_key(str(num)):
                num_count[str(num)] += 1
            else:
                num_count[str(num)] = 1
            if num_count[str(num)] * 2 > numbers_length:
                return num
        return 0

        # 看到的一个思路

        # 链接：https: // www.nowcoder.com / questionTerminal / e8a1b01a2df14cb2b228b30ee6a92163
        # 来源：牛客网
        # 
        # 数组排序后，如果符合条件的数存在，则一定是数组中间那个数。
        # （比如：1，2，2，2，3；或2，2，2，3，4；或2，3，4，4，4 等等）
        # 这种方法虽然容易理解，但由于涉及到快排sort，其时间复杂度为O(NlogN)
        # 并非最优；