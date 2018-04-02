#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        result = []
        rest_val = expectNumber - root.val
        left_path = self.FindPath(root.left, rest_val)
        right_path = self.FindPath(root.right, rest_val)
        for path in left_path+right_path:
            result.append([root.val]+path)
        return result
