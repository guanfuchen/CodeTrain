#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 参考[513. Find Bottom Left Tree Value.py](https://github.com/WuLC/LeetCode/blob/master/Algorithm/Python/513.%20Find%20Bottom%20Left%20Tree%20Value.py)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 层序遍历
        result = root.val
        curr_row = [root]
        while curr_row:
            next_row = []
            for node in curr_row:
                print(node.val)
                if node.left is not None:
                    next_row.append(node.left)
                if node.right is not None:
                    next_row.append(node.right)
            result = curr_row[0].val
            curr_row = next_row
        return result
