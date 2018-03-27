# -*- coding:utf-8 -*-
class Solution:
    """题目描述

    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
    输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
    例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。

    NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
    """

    def minNumberInRotateArray(self, rotateArray):
        # 边界判断
        if not rotateArray:
            return 0

        if len(rotateArray) == 1:
            return rotateArray[0]

        # 遍历就不写了
        # pass

        # min也没啥意思..
        # return min(rotateArray)

        # 查找题目:一般都是二分法最快
        # 这个数组也相当于一个部分有序的数组

        # 最小的数一定有一个特性,即左边右边都要比他大
        # 如果 start < mid 则 说明从start 到 mid 都是选择之后的数组 则应去搜索 后半段
        #   即start-mid 区间是一个递增序列
        # 如果 start > mid 则说明 start 到 mid 之间一定有最小值 :
        #   即start-mid 区间仍然是一个选择数组,应该继续比对
        # 一直保持 start 在前面旋转的区间中 end 在后面的区间中
        # 则最后一定会发生 start 与 end 相邻的情况 则 end 一定是最小值

        # 这个题有相同的数组情况 会有 {1,1,1,0,1,1} 这种情况,若mid == end 时,直接顺序查找即可

        start = 0
        end = len(rotateArray) - 1

        while start != end - 1:
            mid = (start + end) / 2
            if rotateArray[start] < rotateArray[mid]:
                start = mid  # 这里+1会出现问题 有可能出现 start 下标即为最小值的情况
            elif rotateArray[start] > rotateArray[mid]:
                end = mid

            else:  # rotateArray[start] = rotateArray[mid]
                return min(rotateArray[start:end + 1])

        return rotateArray[end]


if __name__ == '__main__':
    t = [6501, 6828, 6963, 7036, 7422, 7674, 8146, 8468, 8704, 8717, 9170, 9359, 9719, 9895, 9896, 9913, 9962, 154, 293,
         334, 492, 1323, 1479, 1539, 1727, 1870, 1943, 2383, 2392, 2996, 3282, 3812, 3903, 4465, 4605, 4665, 4772, 4828,
         5142, 5437, 5448, 5668, 5706, 5725, 6300, 6335]
    Solution().minNumberInRotateArray(t)
