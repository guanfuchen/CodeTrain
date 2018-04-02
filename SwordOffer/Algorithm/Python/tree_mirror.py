#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 操作给定的二叉树，将其变换为源二叉树的镜像。

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        def dfs(root):
            if root is None:
                return None
            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
            return root
        return dfs(root)
