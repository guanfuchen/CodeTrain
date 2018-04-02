#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入一个链表，输出该链表中倒数第k个结点。

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        # 头结点为空的情况
        if head is None:
            return None
        # k为非正数的情况
        if k <= 0:
            return None
        stack_val = []
        while head:
            stack_val.append(head)
            head = head.next

        # k越界的情况
        try:
            stack_val_last_k = stack_val[-k]
            return stack_val_last_k
        except:
            return None
