# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
    """

    # 这个题感觉难点在于当最小的元素被弹出的时候,怎么再去寻找第二小的元素
    # 如果借助其他东西存储元素 空间复杂度则接近O(n) 存储最小的 x个值？都弹栈之后重新构造存储？
    # 若遍历栈寻找 则时间复杂度接近O(n)

    # 只有o(1)的算法才能过
    # 用一个辅助栈 ,记录当前最小元素,当进栈元素小于辅助栈顶元素是，一起进栈 否则只进内部的栈
    # 当弹出元素与辅助栈栈顶元素向时，（代表弹出元素是当前的最小元素） 两个栈一起弹栈
    def __init__(self):
        # 列表当栈用
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        if not self.min_stack or self.min_stack[-1] >= node:
            self.min_stack.append(node)

    def pop(self):
        top_item = self.stack.pop()
        if top_item == self.min_stack[-1]:
            self.min_stack.pop()
            
    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]
