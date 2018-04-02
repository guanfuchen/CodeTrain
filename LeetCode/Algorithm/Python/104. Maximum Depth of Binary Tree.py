#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr_row = [root]
        tree_depth = 0
        if root is None:
            return tree_depth
        while curr_row:
            tree_depth += 1
            next_row = []
            for node in curr_row:
                if node.left is not None:
                    next_row.append(node.left)
                if node.right is not None:
                    next_row.append(node.right)
            curr_row = next_row
        return tree_depth
