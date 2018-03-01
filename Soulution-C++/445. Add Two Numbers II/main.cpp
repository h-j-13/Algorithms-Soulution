#include <iostream>
#include <stack>

using namespace std;
// 445. Add Two Numbers II

// You are given two non-empty linked lists representing two non-negative integers.
// The most significant digit comes first and each of their nodes contain a single digit.
// Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.


// 可以结合翻转链表的题 ，先把l1,l2 翻转,这样题目就变成了LeetCode 2 题 ,最后再把链表翻转过来,感觉比较麻烦
//
// 也可以先算出两个链表的长度，再等到两个链表长度一样是在进行相加。并用前后两个指针处理进位问题，但这样也绕不开翻转链表
// 因为一旦有进很多位的情况，必须需要n个指针才能完成顺序链表的进位。
// 但是我们可以借助其他数据结构，比如数组来存储两个链表表示的数字。
// 最后从低位每项相加并处理进位来得到结果链表
// 总之，翻转顺序是本题的关键（因为链表无法追溯到前面的节点，而进位需要不断向前处理。这是本体的难点）
// 一开始并未设想到链表很长的情况，直接把他们转换成数字再相加并生成结果是不可取的。必须借助其他数据结构
// 这是时候，看到了一个非常好的思路，使用栈来处理数字相加，从高位到低位进栈。再取出处理的是时候就完成了本题的翻转。
// 可以说是一个非常巧妙的思路。



struct ListNode
{
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL)
    {}
};


class Solution
{

public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {   // 使用栈来解决本题

        stack<int> s1, s2;
        while(l1 != NULL) { s1.push(l1->val);l1 = l1->next; }
        while(l2 != NULL) { s2.push(l2->val);l2 = l2->next; }

        ListNode *p = new ListNode(0);
        ListNode *head = NULL;
        int sum = 0;
        int carry = 0;

        while(!s1.empty() || !s2.empty() || carry)
        {
            sum = 0;
            if(!s1.empty()) { sum += s1.top();s1.pop(); }
            if(!s2.empty()) { sum += s2.top();s2.pop(); }
            if(carry != 0) sum += carry;

            carry = sum >= 10;

            p->val = sum % 10;
            head = new ListNode(0);
            head->next = p;
            p = head;
        }

        return p->next;
    }

    // 先遍历链表取出数据相加,最后构造返回链表 O(2n)
    ListNode *addTwoNumbers_fail(ListNode *l1, ListNode *l2)
    {// 测试样例里面会有特别大的数字,int long long 均不能满足要求
        // 获取链表值并相加
        int v1 = 0, v2 = 0, result_v;
        while(l1 != NULL)
        {
            v1 + l1->val;
            l1 = l1->next;
            v1 *= 10;
        }
        v1 /= 10;
        while(l2 != NULL)
        {
            v2 + l2->val;
            l2 = l2->next;
            v2 *= 10;
        }
        v2 /= 10;
        result_v = v1 + v2;

        // 根据相加结果构造新链表
        if(result_v == 0)
            return new ListNode(0);
        else
        {
            ListNode result(0);
            ListNode *pre = NULL;
            ListNode *n = NULL;
            while(result_v != 0)
            {// 从低位向高位生成
                n = new ListNode(result_v % 10);
                n->next = pre;
                pre = n;
                result_v /= 10;
            }
            return n;
        }
    }
};

// 看了下讨论区 基本都是这个思路
// 要想写的比较短 可以使用  value = condition ？ true_value ： false_value 的写法
// 链表题 一般会创建一个空间表 和一个指向这个链表的指针 来进行操作
// ListNode result(0);
// ListNode* p = &result;
// 通过 p.next = ... 来操作这个链表进行增删

int main()
{
    std::cout << "Hello, World!" << std::endl;
}
