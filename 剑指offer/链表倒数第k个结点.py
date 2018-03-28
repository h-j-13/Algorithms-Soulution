# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # 想要知道链表倒数第k的元素 就一定要知道链表尾（链表长度）
        # 由于链表的特性，一定是 O(n)
        # 当然可以把链表按序存成一个列表　然后直接list[-k] 或者简单优化一下空间 使用一个长k的队列,当遍历到链表尾时，要对尾元素一定是所求元素
        # 再优化一下 就是两个相隔k-1的指针，到第一个指针到末尾时候，第二个指针一定指向了倒数第k的元素 时间O(n) 空间O(2)

        if k == 0:  # 边界判断
            return None

        frist_cur = head
        k_cur = None
        k -= 1
        while frist_cur != None:
            if k > 0:  # k>0
                k -= 1
            elif k == 0:  # k=0 k_cur出发
                k_cur = head
                k -= 1
            else:  # k<0(k=-1) k_cur 前进
                k_cur = k_cur.next

            frist_cur = frist_cur.next

        return k_cur


if __name__ == '__main__':
    s = ListNode(10)
    h = s
    s.next = ListNode(2)
    s = s.next
    s.next = ListNode(3)
    s = s.next
    s.next = ListNode(4)
    s = s.next
    s.next = ListNode(5)
    s = s.next

    print Solution().FindKthToTail(h, 2)
