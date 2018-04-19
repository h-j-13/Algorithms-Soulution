#!/usr/bin/env python
# encoding:utf-8

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative_flag = False
        if x < 0:
            negative_flag = True

        s = str(x).replace('-', '')
        # Python还要加个范围检测.
        ans = -int(s[::-1]) if negative_flag else int(s[::-1])
        return ans if ans < 2147483648 and ans >= -2147483648 else 0
