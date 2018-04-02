#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 不断右移计算1的个数，直至最大整数位
class Solution:
    def NumberOf1(self, n):
        # write code here
        return sum([(n >> i & 1) for i in range(0, 32)])

if __name__ == '__main__':
    n = -1
    s = Solution()
    print(s.NumberOf1(n))
