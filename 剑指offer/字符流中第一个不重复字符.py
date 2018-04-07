# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述
    请实现一个函数用来找出字符流中第一个只出现一次的字符。
    例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
    当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

    输出描述:
    如果当前字符流没有存在出现一次的字符，返回#字符。
    """

    # 返回对应char
    def __init__(self):
        # 感觉本题的关键就在于如何使用什么数据结构快速的找到之前是否存储过这个字符
        # 有序hash表感觉不错。可惜python2的dict是无序的 只有python3的dcit是默认有序
        # 感觉这里用hash+链表的方式来实现会比较好 或者 类似redis跳表的实现方式
        # 简单用python的list实现一个这个题吧
        self.letter_hash = {}
        self.letter_list = []

    def FirstAppearingOnce(self):
        if not self.letter_list:
            return '#'
        else:
            return self.letter_list[0]

    def Insert(self, char):
        if not self.letter_hash.has_key(char):
            if char not in self.letter_list:
                self.letter_list.append(char)
            else:
                self.letter_list.remove(char)
                self.letter_hash[char] = 1

        # 其实感觉这里如果用别的数据结构应该会更快
        # 在有序hash表中只保留出现一次的情况


if __name__ == '__main__':
    S = Solution()
    for char in 'google':
        S.Insert(char)
        print S.FirstAppearingOnce(),
