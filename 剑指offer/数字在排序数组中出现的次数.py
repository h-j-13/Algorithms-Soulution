# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    统计一个数字在排序数组中出现的次数。
    """

    def GetNumberOfK(self, data, k):
        # 一提到排序数组 就应该想到二分查找
        # 边界判断
        if not data:
            return 0

        # 二分查找
        start = 0
        end = len(data) - 1
        while start <= end:
            mid = (start + end) / 2
            if data[mid] == k:
                break  # 保存找到k的下标号mid
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        # 边界判断
        if data[mid] != k:
            return 0

        # 向左向右查找是否相同
        count = 1
        left = mid - 1
        while left >= 0 and data[left] == k:
            count += 1
            left -= 1
        right = mid + 1
        while right < len(data) and data[right] == k:
            count += 1
            right += 1
        return count


if __name__ == '__main__':
    print Solution().GetNumberOfK([1, 2, 3, 3, 3, 3], 3)
