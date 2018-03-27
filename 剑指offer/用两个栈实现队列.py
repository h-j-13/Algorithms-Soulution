# -*- coding:utf-8 -*-

class Solution:
    """
    题目描述

    用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
    """

    def __init__(self):
        # 用list模拟stack
        # 只允许调用 append() 与 pop()方法
        # 思路就是一个作栈作为入口
        # 一个栈作为出口
        # 当需要出对的时候 将 入口栈所有的数据元素倒入出口栈
        # 由于栈的特性,这里出口栈的元素出栈顺序即为入口栈的元素入栈顺序
        # 特别注意:只有当出口栈倒空时,才能将入口栈元素导入 否则会破坏元素顺序
        self.list_push = []
        self.list_pop = []

    def push(self, node):
        self.list_push.append(node)

    def pop(self):
        if not self.list_pop: # 当出栈为空时,到栈
            while self.list_push:
                self.list_pop.append(self.list_push.pop())
        # 弹出出栈顶元素即为需要出队的元素
        return self.list_pop.pop()
