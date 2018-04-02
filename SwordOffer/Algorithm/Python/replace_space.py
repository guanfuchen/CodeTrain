#!/usr/bin/python
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s_replace = s.replace(' ', '%20')
        print(s_replace)


while True:
    try:
        s = Solution()
        input_str = raw_input()
        s.replaceSpace(input_str)
    except:
        break
