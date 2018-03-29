# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述

    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
    如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
    """

    # BST后续遍历序列的性质 {左子树(比根小)} - {右子树(比根大)} - 根
    def VerifySquenceOfBST(self, sequence):
        # 边界判断
        if len(sequence) == 0:
            return False  # 87.5% 报错之后添加，没感觉空树不是BST啊...
        else:
            return self.VerifySquenceOfBST_1(sequence)

    def VerifySquenceOfBST_1(self, sequence):
        # 递归出口
        if len(sequence) <= 1:
            return True

        root = sequence[-1]
        left = []
        right = []
        # 划分序列
        if sequence[0] < root:
            for i in sequence[:-2]:  # 除去根后的序列
                if i < root:
                    left.append(i)
                else:
                    right = sequence[sequence.index(i):-2]
                    break
        else:
            right = sequence[:-2]

        # 有可能出现问题的是右边的序列
        if right == [] or min(right) > root:  # 右边序列的最小值都比根大，满足条件，在判别左子树与右子树序列
            return self.VerifySquenceOfBST_1(left) and self.VerifySquenceOfBST_1(right)
        else:
            return False


# 讨论区里看见一个比较好的非递归实现-Java

# 链接：https://www.nowcoder.com/questionTerminal/a861533d45854474ac791d90e447bafd
# 来源：牛客网
#
# //非递归 
# //非递归也是一个基于递归的思想：
# //左子树一定比右子树小，因此去掉根后，数字分为left，right两部分，right部分的
# //最后一个数字是右子树的根他也比左子树所有值大，因此我们可以每次只看有子树是否符合条件
# //即可，即使到达了左子树左子树也可以看出由左右子树组成的树还想右子树那样处理
#  
# //对于左子树回到了原问题，对于右子树，左子树的所有值都比右子树的根小可以暂时把他看出右子树的左子树
# //只需看看右子树的右子树是否符合要求即可

# class Solution {
# public:
#     bool VerifySquenceOfBST(vector<int> sequence) {
#         int size = sequence.size();
#         if(0==size)return false;
#  
#         int i = 0;
#         while(--size)
#         {
#             while(sequence[i++]<sequence[size]);
#             while(sequence[i++]>sequence[size]);
#  
#             if(i<size)return false;
#             i=0;
#         }
#         return true;
#     }
# };