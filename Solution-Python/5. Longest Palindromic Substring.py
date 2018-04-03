#!/usr/bin/env python
# encoding:utf-8

# 2018 4.3 华为机试第一题
class Solution(object):
    def compareStr(self, s, start, end):
        """
        判断以此为中点的最长回文串长度
        :param s: 输入串
        :param start: 起始位置
        :param end: 结束位置 【通过起始位置与决策位置确定中点】
        :return: 最大回文串长度
        """
        L = start
        R = end
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # init
        start = 0
        end = 0
        s_length = len(s)
        # 边界判断

        # 从中间开始检测能不能以此下标生成会文串
        # 对于n长的str 共检测2n-1次 aa 与 aba的情况
        for i in xrange(s_length):
            len1 = self.compareStr(s, i, i)
            len2 = self.compareStr(s, i, i + 1)
            length = max(len1, len2)
            if length > (end - start):
                start = i - (length - 1) / 2
                end = i + length / 2

        return s[start:end + 1]
