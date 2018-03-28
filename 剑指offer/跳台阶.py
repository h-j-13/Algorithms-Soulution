# -*- coding:utf-8 -*-

class Solution:
    """
    题目描述

    一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
    """

    def __init__(self):
        # 加个缓存提高速度
        self.cache = {'0': 0,
                      '1': 1,
                      '2': 2}

    def jumpFloor(self, number):
        # 跳上 n 阶楼梯的跳法 = 【跳上 n - 1 阶楼梯的跳法,(跳1阶) + 跳上 n - 2 阶楼梯的跳法(跳2阶)】
        # 其实是一个斐波那契数列
        # 但是如果不加缓存，会timeout
        if self.cache.has_key(str(number)):
            return self.cache[str(number)]
        else:
            self.cache[str(number)] = self.jumpFloor(number - 1) + self.jumpFloor(number - 2)
            return self.cache[str(number)]
