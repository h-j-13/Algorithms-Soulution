# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # 如果是只有一个只出现一次的元素 利用异或的性质就很容易找到
        # 若是有两个 则数组依次亦或的结果一定是 aXORb
        # 利用 aXORb的结果将之前的数据分为两部分 (以aXORb的第一个1作为数组划分条件，每个数据再同 0000...1...00 进行亦或
        # 这样 a 和 b 一定在两个不同的数组中再依次亦或即得结果
        # O(2n) O(1)
        # 利用亦或性质 a XOR a = 0 进行去重是非常常见的操作

        # 边界判断
        if not array:
            return []
        elif len(array) <= 2:
            return array

        # xor
        temp = reduce(lambda x, y: x ^ y, array)

        # 找到第一个1的位置
        index = 0
        while temp and index <= 32:
            index += 1
            temp = temp >> 1

        # 再找a和b
        a = 0
        b = 0
        for number in array:
            if self.bitis1(number, index):
                a ^= number
            else:
                b ^= number
        return [a, b]

    def bitis1(self, n, i):
        # 检测第n位是否为1
        n = n >> (i - 1)
        return n & 1
