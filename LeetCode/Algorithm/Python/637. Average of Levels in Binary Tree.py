#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        curr_row = [root]
        average_row = []
        while curr_row:
            next_row = []
            curr_row_sum = 0
            for node in curr_row:
                curr_row_sum += node.val
                if node.left is not None:
                    next_row.append(node.left)
                if node.right is not None:
                    next_row.append(node.right)
            # print('curr_row_sum:', curr_row_sum)
            curr_row_average = curr_row_sum * 1.0 / len(curr_row)
            # print('curr_row_average:', curr_row_average)
            average_row.append(curr_row_average)
            curr_row = next_row
        return average_row
