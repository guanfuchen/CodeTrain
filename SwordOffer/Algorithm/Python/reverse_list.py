#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入一个链表，反转链表后，输出链表的所有元素。
# 遍历链表，从后往前修改next，最后一个结点next置空即可

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None
        node_stack = []
        while pHead:
            node_stack.append(pHead)
            pHead = pHead.next
        node_len = len(node_stack)

        for node_index in range(node_len - 1, 0, -1):
            node_stack[node_index].next = node_stack[node_index - 1]
        node_stack[0].next = None
        return node_stack[-1]
