#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。

class Solution:
    def __init__(self):
        self.stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)

    def pop(self):
        # write code here
        return self.stack.pop()

    def top(self):
        # write code here
        return len(self.stack) - 1

    def min(self):
        # write code here
        return min(self.stack)
