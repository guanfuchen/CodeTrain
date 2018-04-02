# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        out_list_val = []
        if listNode is None:
            return out_list_val
        listNodeNext = listNode.next
        val = listNode.val
        while listNodeNext is not None:
            out_list.append(val)
            listNodeNext = listNodeNext.next
        return out_list_val[::-1]


while True:
    try:
        listNode = eval(raw_input())
        s = Solution()
        print(s.printListFromTailToHead(listNode))
    except:
        break