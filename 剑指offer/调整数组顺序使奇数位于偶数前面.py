# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        """
        题目描述

        输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
        并保证奇数和奇数，偶数和偶数之间的相对位置不变。
        """

        # 一个类似排序的题
        # 题目中的稳定性要求直接否决了类似快速排序的交换方式
        # 在基础排序中,只有冒泡，插入，归并是稳定的（没有进行间隔交换）
        # 试着采用类似插入排序的调整方法

        length = len(array)

        if length <= 1:
            return array

        for i in xrange(0, length):
            if array[i] % 2 == 0:  # 当该位不是奇数,则找到后面第一个奇数,并两两相邻交换过来。 若后面全都是偶数,这排序完成
                j = i + 1
                found_odd = False
                while j < length:
                    if array[j] % 2 == 1:
                        found_odd = True
                        break
                    j += 1

                if not found_odd:
                    return array
                else:
                    while j > i:
                        # print  j
                        array[j - 1], array[j] = array[j], array[j - 1]  # swap
                        j -= 1

        return array

        # 看了下讨论区
        # 有一个用空间换时间的答案，用到了deque(双端队列)
        from collections import deque
        odd = deque()
        x = len(array)
        for i in range(x):
            if array[x - i - 1] % 2 != 0:  # 倒序扫描，奇数正向加载前面
                odd.appendleft(array[x - i - 1])
            if array[i] % 2 == 0:
                odd.append(array[i])
        return list(odd)

        # 其实用两个 list 也可以达到同样的效果,而且代码应该更简洁一点
        # 其实第一个就应该想到这个方法的,用空间换时间的思路还是不够熟练啊

        odd = []
        even = []
        for num in array:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return odd + even


if __name__ == '__main__':
    print Solution().reOrderArray([1, 2, 3, 4, 5, 6, 7])
