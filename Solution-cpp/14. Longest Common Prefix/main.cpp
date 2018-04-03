#include <iostream>
#include <vector>
#include <map> 
#include <string.h> 

using namespace std; 

// 14. Longest Common Prefix

// Write a function to find the longest common prefix string amongst an array of strings.

// 最简单的循环 O(n2)
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) 
    {

        if (strs.size() == 0)
            return "";

        string Prefix = "";
        
        for (int i = 0; i < strs[0].size(); i++) 
        {
            for (int j = 1; j < strs.size(); j++) 
            {
                if (strs[j].size() < i || strs[j][i] != strs[0][i])
                    return Prefix;
            }
            Prefix += strs[0][i];
        }
        return Prefix;
    }
};

int main()
{
    std::cout << "Hello, World!" << std::endl;
    Solution s;
    vector<string> test;
    test.push_back("asd");
    test.push_back("asd");
    test.push_back("asd");
    cout<<s.longestCommonPrefix(test);
    return 0;
}