#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        cur_row = [root]
        result = [root.val]
        while cur_row:
            next_row = []
            for node in cur_row:
                if node.left is not None:
                    result.append(node.left.val)
                    next_row.append(node.left)
                if node.right is not None:
                    result.append(node.right.val)
                    next_row.append(node.right)
            cur_row = next_row
        return result
