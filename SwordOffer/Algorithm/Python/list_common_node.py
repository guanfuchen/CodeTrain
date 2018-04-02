#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入两个链表，找出它们的第一个公共结点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return None
        pList1 = pHead1
        pList2 = pHead2

        while pList1:
            while pList2:
                if pList1 == pList2:
                    return pList1
                pList2 = pList2.next
            pList2 = pHead2
            pList1 = pList1.next
        return None
