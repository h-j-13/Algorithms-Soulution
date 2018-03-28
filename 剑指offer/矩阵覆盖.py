# -*- coding:utf-8 -*-

class Solution:
    """
    题目描述

    我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？。
    """

    def __init__(self):
        # 加个缓存提高速度
        self.cache = {'0': 0,
                      '1': 1,
                      '2': 2}

    # 想了一下 实际上和跳台阶问题是一模一样的
    # 问题可以简化为 使用一个 1*2 的矩阵 沿着x轴向右摆放 摆放到长度为n的时候 共有多少种摆放方法
    # （因为一旦横着摆了一个1*2 上面必然会再叠放一个 同样的矩阵，此问题就退化成了求第n项斐波那契数列

    def rectCover(self, number):
        if self.cache.has_key(str(number)):
            return self.cache[str(number)]
        else:
            self.cache[str(number)] = self.rectCover(number - 1) + self.rectCover(number - 2)
            return self.cache[str(number)]
