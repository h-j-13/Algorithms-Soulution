# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
    为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
    但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,
    可以很快的求出任意非负整数区间中1出现的次数。
    """

    def NumberOf1Between1AndN_Solution(self, n):
        # 写了个笨办法

        str_n = [str(i) for i in xrange(1, n + 1)]
        count = 0
        for s in str_n:
            count += s.count('1')
        return count

        # 下面附上剑指offer的解答 , 其实还是这个找规律的数学题
        # https://www.nowcoder.com/questionTerminal/bd7f978302044eee894445e244c7eee6
