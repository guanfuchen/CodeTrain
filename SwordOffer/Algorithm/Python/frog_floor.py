#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

# 动态规划问题
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number==0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2
        else:
            jump_number = []
            jump_number.append(1)
            jump_number.append(2)
            for n in range(2, number):
                jump_number.append(jump_number[n-1]+jump_number[n-2])
            return jump_number[-1]
