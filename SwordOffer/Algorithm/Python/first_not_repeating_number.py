#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置

import collections

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        s_ones = {}
        s_ones_char = []

        for s_single in s:
            if s_single not in s_ones:
                s_ones[s_single] = 1
                s_ones_char.append(s_single)
            else:
                if s_single in s_ones_char:
                    s_ones_char.remove(s_single)
                s_ones[s_single] += 1
        return s.find(s_ones_char[0])

if __name__ == '__main__':
    s = Solution()
    str_input = 'googleo'
    print(s.FirstNotRepeatingChar(str_input))
