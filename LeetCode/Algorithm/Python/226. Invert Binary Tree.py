#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        right_change = None
        left_change = None
        # 递归的思路，将左右也同时用invertTree进行操作
        if root.left is not None:
            right_change = self.invertTree(root.left)
        if root.right is not None:
            left_change = self.invertTree(root.right)
        root.left = left_change
        root.right = right_change
        return root
