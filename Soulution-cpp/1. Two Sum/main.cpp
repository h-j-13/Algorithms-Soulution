#include <iostream>
#include <vector>
#include <map>  

using namespace std; 

// 1. Two Sum

// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// 最简单的双循环 O(n2)
class Solution1 {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        vector<int> result;
        for (int i = 0; i < nums.size(); i++)
            for (int j = 0; j < nums.size();j++)
                if (i!=j && nums[i] + nums[j] == target)
                {
                    result.push_back(i);
                    result.push_back(j);
                    return result
                }
                
};

// hash表 (用空间换时间 hash表的查询基本是o(1),当然碰撞时极端情况下时候会趋向于o(n))
// map : https://www.cnblogs.com/fnlingnzb-learner/p/5833051.html
// 查询时,查询该元素是否能与hashmap中的元素相加为target
// 并不断把元素加入hashmap中,使其只用遍历一遍就能找到结果
class Solution2 {
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        // 无序表 见https://www.cnblogs.com/NeilZhang/p/5724996.html
        unordered_map<int, int> hash;   // 数值-下标   
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            int numberToFind = target - nums[i];    // 需要查询的数字
            if (hash.find(numberToFind) != hash.end()) 
            {
                result.push_back(hash[numberToFind]);
                result.push_back(i);			
                return result;
            }
            hash[nums[i]] = i;
        }
        return result;
    }
                
};

// 还有一种先循环建立map 再找的方法,也行.不过自然没有这个只循环一次的好

// note
// 简单学习一下vector map unordered_map hashtable 等常见STL数据结构
// 学习如何优雅的遍历

// 2018-2-27
int main()
{
    std::cout << "Hello, World!" << std::endl;
    return 0;
}