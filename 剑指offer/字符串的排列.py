# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述
    输入一个字符串,按字典序打印出该字符串中字符的所有排列。
    例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

    输入描述:
    输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
    """

    def Permutation(self, ss, start_index=0):
        # 全排列 = 第一位依次与后面交换(并固定) + 后面字符串全排列
        # 边界
        if len(ss) <= 1:
            return ss
        self.str_premutation = []
        self.f(list(ss), 0)
        # 这里不光要去重,还要根据字典序排序
        self.str_premutation = sorted(list(set(self.str_premutation)))
        return self.str_premutation

    def f(self, ss_list, start_index):
        if start_index == len(ss_list) - 1:  # 只剩下一位,无法交换,直接输出
            self.str_premutation.append("".join(ss_list))
        for i in xrange(start_index, len(ss_list)):
            ss_list[start_index], ss_list[i] = ss_list[i], ss_list[start_index]
            self.f(ss_list, start_index + 1)  # 确定第一位之后,交换后面的位
            ss_list[start_index], ss_list[i] = ss_list[i], ss_list[start_index]  # 将字符串换回来


if __name__ == '__main__':
    print Solution().Permutation('aa')
