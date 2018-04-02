#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number==1:
            return 1
        elif number==2:
            return 2
        else:
            out_floor = []
            out_floor.append(1)
            out_floor.append(2)
            for i in range(2, number):
                out_floor.append(sum(out_floor)+1)
            return out_floor[-1]
