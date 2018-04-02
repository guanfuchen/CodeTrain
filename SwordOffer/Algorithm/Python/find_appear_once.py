#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

import collections

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        res = []
        array_counter = collections.Counter(array).most_common()
        for array_single in array_counter:
            array_num = array_single[0]
            array_time = array_single[1]
            if array_time==1:
                res.append(array_num)

        return res

if __name__ == '__main__':
    s = Solution()
    array = [1, 2, 2, 1, 3, 4]
    print(s.FindNumsAppearOnce(array))
