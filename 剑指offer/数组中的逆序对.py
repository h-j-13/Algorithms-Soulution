# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述
    在数组中的两个数字，如果前面一个数字大于后面的数字，
    则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
    并将P对1000000007取模的结果输出。 即输出P%1000000007

    输入描述:
    题目保证输入的数组中没有的相同的数字

    数据范围：
	对于%50的数据,size<=10^4
	对于%75的数据,size<=10^5
	对于%100的数据,size<=2*10^5
    """

    def InversePairs(self, data):
        # # O(n^2) --- 超时
        # count = 0
        # for i in xrange(len(data)):
        #     for j in xrange(i + 1, len(data)):
        #         if data[i] > data[j]:
        #             count += 1
        # return count % 1000000007
        # https://www.nowcoder.com/questionTerminal/96bd6684e04a44eb80e6a68efc0ec6c5
        pass

        # 这题python一个过的都没有...

        # 附一份Java代码

        #
        # 链接：https://www.nowcoder.com/questionTerminal/96bd6684e04a44eb80e6a68efc0ec6c5
        # 来源：牛客网
        #
        # 代码参考剑指offer
        # ----------------------------------------------------------------
        # 2016.08.02更新
        # class Solution {
        # public:
        #     long long InversePairsCore(vector<int> &data,vector<int>&copy,int start,int end)
        #     {
        #         if(start==end)
        #         {
        #             copy[start]=data[start];
        #             return 0;
        #         }
        #         int length = (end-start)/2;
        #         long long left = InversePairsCore(copy,data,start,start+length);
        #         long long right = InversePairsCore(copy,data,start+length+1,end);
        #            
        #         int i = start + length;
        #         int j = end;
        #         int indexCopy = end;
        #         long long  count=0;
        #         while(i>=start&&j>=start+length+1)
        #         {
        #             if(data[i]>data[j])
        #             {
        #                 copy[indexCopy--]=data[i--];
        #                 count+=j-start-length;
        #             }
        #              
        #             else
        #             {
        #                 copy[indexCopy--]=data[j--];
        #             }
        #         }
        #         for(;i>=start;--i)
        #             copy[indexCopy--] = data[i];
        #         for(;j>=start+length+1;--j)
        #             copy[indexCopy--] = data[j];
        #         return left+right+count;
        #         }
        #     int InversePairs(vector<int> data) {
        #         int length = data.size();
        #         if(length<=0)
        #             return 0;
        #         vector<int> copy;
        #         for(int i=0;i<length;i++)
        #             copy.push_back(data[i]);
        #         long long  count = InversePairsCore(data,copy,0,length-1);
        #         copy.clear();
        #         return count%1000000007;
        #     }
        #       
        #       
        # };
        #