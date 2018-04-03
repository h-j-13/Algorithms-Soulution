#include <iostream>


// You are given two non-empty linked lists representing two non-negative integers.
// The digits are stored in reverse order and each of their nodes contain a single digit.
// Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Definition for singly-linked list.

struct ListNode
{
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL)
    {}
};

// 先遍历链表取出数据相加,最后返回链表 O(2n)
class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        int carry_flag = 0;
        int sum = 0;
        ListNode result(0);
        ListNode* p = &result;

        while(l1||l2||carry_flag)
        {
            sum = 0;
            if(l1!=NULL)
            {
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2!=NULL)
            {
                sum += l2->val;
                l2 = l2->next;
            }
            sum += carry_flag;

            carry_flag = sum >= 10;

            p->next = new ListNode(sum%10);
            p = p->next;
        }
        return result.next;
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
