#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        result = sorted(tinput)[:k]
        return result

if __name__ == '__main__':
    s = Solution()
    tinput = [4,5,1,6,2,7,3,8]
    k = 10
    print(s.GetLeastNumbers_Solution(tinput, k))