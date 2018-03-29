# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
    假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
    但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
    """

    def __init__(self):
        self.stack = []

    def IsPopOrder(self, pushV, popV):
        # 想了半天有关这两个序列的性质与特性.实在是没有什么好的思路
        # 后来干脆就想着自己去利用一个栈 看是否能模拟出出栈序列这样的来判断
        for popV_item in popV:
            if self.stack != [] and self.stack[-1] == popV_item:  # 先栈顶元素是不是下一个出栈的元素
                self.stack.pop()  # 是 -> 则出栈
            else:  # 不是 -> 则元素依次进栈至该元素
                if not pushV:  # 若所有元素都进栈
                    return False  # 则说序列明不可能
                else:  # 元素依次进栈至该元素
                    for _ in xrange(len(pushV)):
                        if pushV[0] == popV_item:
                            pass  # 不做处理,因为进栈还要出栈
                        else:
                            self.stack.append(pushV[0])
                        pushV.pop(0)  # 在带进栈序列中删除该元素
        # 若栈空则表示该序列可行
        return self.stack == []


if __name__ == '__main__':
    print Solution().IsPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
