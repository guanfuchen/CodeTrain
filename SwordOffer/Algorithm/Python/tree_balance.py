#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# 平衡二叉树的定义，左右子树的高度差不超过1，首先计算一个结点的高度，另外遍历root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here

        def height_tree(pRoot):
            if pRoot is None:
                return 0
            left_height = 0
            if pRoot.left:
                left_height = height_tree(pRoot.left)
            right_height = 0
            if pRoot.right:
                right_height = height_tree(pRoot.right)
            return max(left_height, right_height) + 1

        def dfs(pRoot):
            if pRoot is None:
                return True
            left_height = height_tree(pRoot.left)
            right_height = height_tree(pRoot.right)
            if abs(left_height - right_height) > 1:
                return False
            else:
                left_balance = True
                if pRoot.left:
                    left_balance = dfs(pRoot.left)
                right_balance = True
                if pRoot.right:
                    right_balance = dfs(pRoot.right)
                return left_balance and right_balance

        return dfs(pRoot)
