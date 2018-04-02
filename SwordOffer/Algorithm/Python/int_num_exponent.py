#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# 考查点主要是，base和exponent的取值类型，主体是大于0的计算

class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = True
        if base==0:
            return 0
        if exponent==0:
            return 1
        if exponent<0:
            flag = False
        result = 1
        for n in range(abs(exponent)):
            result = base * result
        if flag==False:
            result = 1.0/result
        return result
