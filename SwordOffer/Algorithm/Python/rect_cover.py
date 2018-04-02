#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            cover_num = []
            cover_num.append(1)
            cover_num.append(2)
            for i in range(2, number):
                cover_num.append(cover_num[i - 1] + cover_num[i - 2])
            return cover_num[-1]

