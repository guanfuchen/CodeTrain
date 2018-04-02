#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 is None or pRoot2 is None:
            return False
        return self.is_sub_tree(pRoot1, pRoot2) or self.is_sub_tree(pRoot1.left, pRoot2) or self.is_sub_tree(
            pRoot1.right, pRoot2)

    def is_sub_tree(self, root1, root2):
        if root2 is None:
            return True
        if root1 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.is_sub_tree(root1.left, root2.left) and self.is_sub_tree(root1.right, root2.right)
