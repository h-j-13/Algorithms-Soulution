# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
    """
    # todo 2018.23

    # 这个题感觉难点在于当最小的元素被弹出的时候,怎么再去寻找第二小的元素
    # 如果借助其他东西存储元素 空间复杂度则接近O(n) 存储最小的 x个值？都弹栈之后重新构造存储？
    # 若遍历栈寻找 则时间复杂度接近O(n)
    def __init__(self):
        # 列表当栈用
        self.stack = []
        self.min_dict = {}

    def push(self, node):
        self.stack.append(node)
        if self.min_dict.has_key(str(node)):
            self.min_dict[str(node)] += 1
        else:
            self.min_dict[str(node)] = 1

    def pop(self):
        self.stack.pop()
        if self.min_dict[str(self.top())] > 1:
            self.min_dict[str(self.top())] -= 1
        else:
            self.min_dict.pop(str(self.top()))

    def top(self):
        return self.stack[-1]

    def min(self):
