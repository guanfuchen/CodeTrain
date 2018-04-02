#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        curr_row = [root]
        max_row = []
        if root is None:
            return max_row

        while curr_row:
            next_row = []
            curr_row_max = None
            for node in curr_row:
                if curr_row_max is None:
                    curr_row_max = node.val
                else:
                    if node.val > curr_row_max:
                        curr_row_max = node.val
                if node.left is not None:
                    next_row.append(node.left)
                if node.right is not None:
                    next_row.append(node.right)
            print('curr_row_max:', curr_row_max)
            max_row.append(curr_row_max)
            curr_row = next_row
        return max_row
