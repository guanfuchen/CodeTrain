#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pHead3 = None
        pSaveHead3 = None
        while pHead1 is not None and pHead2 is not None:
            if pHead2.val < pHead1.val:
                if pHead3 is None:
                    pHead3 = ListNode(pHead2.val)
                    pSaveHead3 = pHead3
                else:
                    pHead3.next = ListNode(pHead2.val)
                    pHead3 = pHead3.next
                pHead2 = pHead2.next
            else:
                if pHead3 is None:
                    pHead3 = ListNode(pHead1.val)
                    pSaveHead3 = pHead3
                else:
                    pHead3.next = ListNode(pHead1.val)
                    pHead3 = pHead3.next
                pHead1 = pHead1.next

        while pHead1 is not None:
            if pHead3 is None:
                pHead3 = ListNode(pHead1.val)
                pSaveHead3 = pHead3
            else:
                pHead3.next = ListNode(pHead1.val)
                pHead3 = pHead3.next
            pHead1 = pHead1.next
        while pHead2 is not None:
            if pHead3 is None:
                pHead3 = ListNode(pHead2.val)
                pSaveHead3 = pHead3
            else:
                pHead3.next = ListNode(pHead2.val)
                pHead3 = pHead3.next
            pHead2 = pHead2.next
        return pSaveHead3
