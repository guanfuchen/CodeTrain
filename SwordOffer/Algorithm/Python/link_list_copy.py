#!/usr/bin/python
# -*- coding: UTF-8 -*-

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        pCloneHead = RandomListNode(None)
        pCloneList = pCloneHead
        random_dict = {}
        next_dict = {}
        while pHead:
            pCloneList.next = RandomListNode(pHead.label)
            random_dict[id(pCloneList.next)] = id(pHead.random)
            next_dict[id(pHead.next)] = pCloneList.next
            pCloneList = pCloneList.next
            pHead = pHead.next
        pCloneList = pCloneHead.next
        while pCloneList:
            id_random = random_dict[id(pCloneList)]
            pCloneList.random = next_dict[id_random]
            pCloneList = pCloneList.next
        return pCloneHead.next

if __name__ == '__main__':
    # {1, 2, 3, 4, 5, 3, 5,  # ,2,#}
    pass
