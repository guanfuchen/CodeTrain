#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        cur_node = [pRoot]
        height = 0
        while cur_node:
            next_node = []
            height += 1
            for node in cur_node:
                if node.left is not None:
                    next_node.append(node.left)
                if node.right is not None:
                    next_node.append(node.right)
            cur_node = next_node
        return height
