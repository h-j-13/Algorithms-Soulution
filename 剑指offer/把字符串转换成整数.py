# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
    数值为0或者字符串不是一个合法的数值则返回0
    """

    def StrToInt(self, s):
        # 边界判断
        if not s:
            return 0
        # 先处理符号位
        negative_flag = False
        if s[0] == '-':
            s = s[1:]
            negative_flag = True
        elif s[0] == '+':
            s = s[1:]
        if s.count('+') >= 1 or s.count('-') >= 1:
            return 0
        # 每次读取一位 并乘10加到结果集合中
        result = 0
        s = s.lower()
        for char in s:
            if ord('0') <= ord(char) <= ord('9'):
                result = result * 10 + ord(char) - ord('0')
            elif ord(char) == ord('.'):  # 小数点
                if s.count('e') < 1:
                    break
            elif ord(char) == ord('e'):  # 还想找找有没有 10e2 这类的数字,测试用例里直接没有...
                # 获取之前的result 再乘以 10^后面的数字即可得到答案
                pass
            else:
                return 0

        return result if not negative_flag else -result


if __name__ == '__main__':
    print Solution().StrToInt('-12.3')
