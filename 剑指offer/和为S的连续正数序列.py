# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
    但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
    没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
    现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

    输出描述:
    输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
    """

    def f(self, start, end):
        return (start + end) * (end - start + 1) / 2

    # 优化一下下面的写法
    def FindContinuousSequence(self, tsum):
        # init
        left = 1
        right = 2
        result = []
        while left < tsum:
            temp = self.f(left, right)
            if temp == tsum:
                right += 1
                result.append(range(left, right))

            elif temp > tsum:
                left += 1
            else:
                right += 1
        return result

if __name__ == '__main__':
    Solution().FindContinuousSequence(10)

    # 内存超了
    # def FindContinuousSequence(self, tsum):
    #     # 边界判断
    #     if tsum <= 0:
    #         return []
    #     # 为了方便操作建立一个 1~tsum 的list
    #     numbers = [i for i in xrange(1, tsum + 1)]
    #     # 维护两个指针标识连续序列的范围
    #     left = 0
    #     right = 0
    #     result = []
    #     while left <= right and left <= tsum:
    #         temp = sum(numbers[left:right])
    #         if temp == tsum:
    #             result.append(numbers[left:right])
    #         elif temp > tsum:
    #             left += 1
    #         else:
    #             right += 1
    #     return result

# 其实也可以用数学公式
# 链接：https://www.nowcoder.com/questionTerminal/c451a3fd84b64cb19485dad758a55ebe
# 来源：牛客网
#
#       //根据数学公式计算:(a1+an)*n/2=s  n=an-a1+1
#       //(an+a1)*(an-a1+1)=2*s=k*l(k>l)
#       //an=(k+l-1)/2  a1=(k-l+1)/2