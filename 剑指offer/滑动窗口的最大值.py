# -*- coding:utf-8 -*-

class Solution:
    """
    题目描述

    给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
    例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
    那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
    针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
    {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}，
    {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}，
    {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
    """

    def maxInWindows(self, num, size):
        # 边界判断
        if size <= 0 or size > len(num):
            return []
        # init
        windows = num[:size]    # 切片操作是左闭右开 ！！！
        print windows
        max_num = max(windows)
        result = [max_num]
        # 循环比对最大值
        for i in xrange(size, len(num)):  # 循环遍历每一个要进入滑动窗口的元素
            if num[i] <= max_num and max_num > windows[0]:  # 进入的元素和出去的元素小于最大值
                result.append(max_num)
                windows.append(num[i])
                windows.pop(0)
            elif num[i] > max_num:  # 进入的元素比最大值还大
                max_num = num[i]
                result.append(max_num)
                windows.append(num[i])
                windows.pop(0)
            else:  # 其他情况 - 直接重新计算最大值
                windows.append(num[i])
                windows.pop(0)
                max_num = max(windows)
                result.append(max_num)
        return result


if __name__ == '__main__':
    print Solution().maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3)
