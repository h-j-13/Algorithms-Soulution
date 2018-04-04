# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目描述

    输入一棵二叉树，判断该二叉树是否是平衡二叉树。
    """

    # 获取树的深度
    def TreeDepth(self, pRoot):
        # 边界判断
        depth = 0
        if not pRoot:
            return depth
        # 层序遍历
        pre_node_list = [pRoot]
        while pre_node_list:
            node_list = []
            for node in pre_node_list:
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
            pre_node_list = node_list
            depth += 1

        return depth

    def IsBalanced_Solution(self, pRoot):
        # 边界判断
        if not pRoot:
            return True
        # 判断左右子树深度差值是否绝对值小于1 并且 左右子树也是AVL树
        return abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) <= 1 and \
               self.IsBalanced_Solution(pRoot.left) and \
               self.IsBalanced_Solution(pRoot.right)

    # discuss 区的思路
    # 从上往下求深度的时候,每个节点会判断很多次
    # 应该从下往上判断深度
    # 当然需要先遍历二叉树

    # 链接：https: // www.nowcoder.com / questionTerminal / 8
    # b3b95850edb4115918ecebdf1b4d222
    # 来源：牛客网
    #
    # public
    #
    # class Solution {
    #      // 后续遍历时，遍历到一个节点，其左右子树已经遍历  依次自底向上判断，每个节点只需要遍历一次
    #      
    #     private boolean isBalanced=true;
    #     public boolean IsBalanced_Solution(TreeNode root) {
    #          
    #         getDepth(root);
    #         
    #
    # return isBalanced;
    #     }
    #     public
    # int
    # getDepth(TreeNode
    # root){
    #         if (root == null)
    #                 return 0;
    #         int
    # left = getDepth(root.left);
    #         int
    # right = getDepth(root.right);
    #          
    #         if (Math.abs(left - right) > 1){
    #             isBalanced=false;
    #         }
    #         return right > left ?right + 1:left + 1;
    #          
    #     }
    # }