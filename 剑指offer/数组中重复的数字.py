# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    在一个长度为n的数组里的所有数字都在0到n-1的范围内。
    数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
    例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
    """

    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # 长度和数值范围有限定，查重复
        # 用hash解决应该是比较快的方法 O(n) O(n)
        numbers_length = len(numbers)
        # hash表 hash函数 = hash(n) = n
        hash = [0 for i in xrange(numbers_length)]

        for number in numbers:
            if hash[number]:
                # 这里的 duplication 是传入的一个列表,需要注意一下
                duplication.insert(0, number)
                return True
            else:
                hash[number] = 1
        return False

        # O(n) O(1) 的解法
        # 利用本身数组来构成一个hash表解决问题
        # 链接：https: // www.nowcoder.com / questionTerminal / 623
        # a5ac0ea5b4e5f95552655361ae0a8
        # 来源：牛客网
        #
        # 不需要额外的数组或者hash
        # table来保存，题目里写了数组里数字的范围保证在0 ~ n - 1
        # 之间，所以可以利用现有数组设置标志，当一个数字被访问过后，
        # 可以设置对应位上的数 + n，之后再遇到相同的数时，
        # 会发现对应位上的数已经大于等于n了，那么直接返回这个数即可。
